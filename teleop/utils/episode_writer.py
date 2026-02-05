"""
episode_writer.py - Moduł do nagrywania danych teleoperation
===========================================================

Ten moduł jest odpowiedzialny za zapisywanie wszystkich danych z sesji teleoperation do plików.
Dane te mogą być później użyte do:
- Uczenia maszynowego (imitation learning)
- Analizy ruchów robota
- Odtwarzania i debugowania
- Tworzenia zestawów danych treningowych

DLA POCZĄTKUJĄCYCH:
- Episode (epizod) = jedna sesja nagrywania od naciśnięcia 's' do ponownego naciśnięcia 's'
- Każdy epizod zawiera: obrazy z kamer, pozycje stawów, stany dłoni, timestampy
- Dane są zapisywane w strukturze katalogów: task_dir/episode_XXX/
"""

import os
import cv2          # OpenCV - biblioteka do przetwarzania obrazów
import json         # Do zapisywania metadanych w formacie JSON
import datetime     # Do znaczników czasowych
import numpy as np  # Do operacji na tablicach liczb (pozycje stawów, etc.)
import time
from .rerun_visualizer import RerunLogger  # Do wizualizacji nagrań w czasie rzeczywistym
from queue import Queue, Empty              # Do asynchronicznego przetwarzania danych
from threading import Thread                # Do działania w tle
import logging_mp
logger_mp = logging_mp.get_logger(__name__)

class EpisodeWriter():
    """
    Klasa do nagrywania i zapisywania epizodów teleoperation.
    
    Główne funkcje:
    1. Tworzy strukturę katalogów dla każdego epizodu
    2. Zapisuje obrazy z kamer jako pliki wideo (MP4)
    3. Zapisuje dane stawów jako pliki NumPy (NPZ)
    4. Zapisuje metadane jako JSON
    5. Opcjonalnie wizualizuje dane w czasie rzeczywistym (Rerun)
    
    Dla początkujących - Co zapisujemy:
    - Obrazy z kamer głowy i nadgarstków (30 FPS)
    - Pozycje wszystkich stawów robota (kąty)
    - Stany dłoni zręcznościowych (pozycje palców)
    - Akcje wysłane do robota
    - Metadane (data, czas, cel zadania, etc.)
    """
    
    def __init__(self, task_dir, task_goal=None, task_desc = None, task_steps = None, frequency=30, image_size=[640, 480], rerun_log = True):
        """
        Inicjalizuje EpisodeWriter.
        
        Args:
            task_dir (str): Katalog główny gdzie zapisywać dane (np. './data/pick_cube/')
            task_goal (str): Cel zadania (np. "Podnieś czerwony kubek")
            task_desc (str): Opis zadania (np. "Robot podnosi kubek ze stołu")
            task_steps (str): Kroki zadania (np. "1: Zbliż rękę, 2: Chwyć, 3: Podnieś")
            frequency (int): Częstotliwość nagrywania w Hz (klatek na sekundę)
            image_size (list): Rozmiar obrazów [szerokość, wysokość]
            rerun_log (bool): Czy włączyć wizualizację w czasie rzeczywistym
            
        Dla początkujących:
        Ta funkcja przygotowuje wszystko do nagrywania:
        - Tworzy katalogi jeśli nie istnieją
        - Znajduje numer ostatniego epizodu (aby kontynuować numerację)
        - Inicjalizuje kolejkę do przetwarzania danych w tle
        - Uruchamia wątek roboczy do zapisywania
        """
        logger_mp.info("==> EpisodeWriter inicjalizacja...\n")
        self.task_dir = task_dir  # Gdzie zapisywać dane
        
        # Teksty opisujące zadanie (zapisywane w metadanych)
        self.text = {
            "goal": "Podnieś czerwony kubek ze stołu.",    # Cel zadania
            "desc": "opis zadania",                        # Szczegółowy opis
            "steps":"krok1: zrób to; krok2: zrób tamto; ...",  # Instrukcje krok po kroku
        }
        
        # Nadpisz domyślne teksty jeśli użytkownik podał własne
        if task_goal is not None:
            self.text['goal'] = task_goal
        if task_desc is not None:
            self.text['desc'] = task_desc
        if task_steps is not None:
            self.text['steps'] = task_steps

        self.frequency = frequency      # Jak często zapisujemy ramki (30 Hz = 30 razy na sekundę)
        self.image_size = image_size    # Rozmiar obrazów do zapisania

        # Opcjonalna wizualizacja w czasie rzeczywistym (Rerun)
        self.rerun_log = rerun_log
        if self.rerun_log:
            logger_mp.info("==> RerunLogger inicjalizacja...\n")
            # Rerun to narzędzie do wizualizacji danych robotycznych w 3D
            self.rerun_logger = RerunLogger(prefix="online/", IdxRangeBoundary = 60, memory_limit = "300MB")
            logger_mp.info("==> RerunLogger inicjalizacja zakończona.\n")
        
        # ID liczniki
        self.item_id = -1      # ID aktualnej ramki w epizodzie
        self.episode_id = -1   # ID aktualnego epizodu
        
        # Znajdź ostatni numer epizodu jeśli katalog już istnieje
        if os.path.exists(self.task_dir):
            # Znajdź wszystkie katalogi episode_XXX (ale nie .zip)
            episode_dirs = [episode_dir for episode_dir in os.listdir(self.task_dir) 
                           if 'episode_' in episode_dir and not episode_dir.endswith('.zip')]
            # Posortuj i weź ostatni (największy numer)
            episode_last = sorted(episode_dirs)[-1] if len(episode_dirs) > 0 else None
            # Wyciągnij numer z nazwy (np. "episode_5" -> 5)
            self.episode_id = 0 if episode_last is None else int(episode_last.split('_')[-1])
            logger_mp.info(f"==> Katalog task_dir już istnieje, obecny self.episode_id to:{self.episode_id}\n")
        else:
            # Utwórz katalog jeśli nie istnieje
            os.makedirs(self.task_dir)
            logger_mp.info(f"==> Katalog epizodów nie istnieje, tworzę nowy.\n")
        
        # Przygotuj metadane
        self.data_info()

        # === SYSTEM KOLEJKI DO PRZETWARZANIA W TLE ===
        # Dlaczego kolejka? Zapisywanie danych na dysk jest wolne.
        # Gdybyśmy zapisywali bezpośrednio w głównej pętli, spowolniłoby to sterowanie robotem!
        # Zamiast tego, dane są dodawane do kolejki, a osobny wątek zapisuje je w tle.
        
        self.is_available = True  # Czy klasa jest gotowa do przyjmowania nowych danych
        
        # Kolejka FIFO (First In First Out) - pierwsze dane wchodzą, pierwsze wychodzą
        self.item_data_queue = Queue(-1)  # -1 = nieograniczony rozmiar
        self.stop_worker = False          # Flaga do zatrzymania wątku roboczego
        self.need_save = False            # Czy trzeba zapisać epizod
        
        # Uruchom wątek roboczy w tle
        self.worker_thread = Thread(target=self.process_queue)
        self.worker_thread.start()

        logger_mp.info("==> EpisodeWriter zainicjalizowany pomyślnie.\n")
    
    def is_ready(self):
        """
        Sprawdza czy EpisodeWriter jest gotowy do przyjmowania danych.
        
        Returns:
            bool: True jeśli gotowy, False jeśli zajęty
            
        Dla początkujących:
        Ta metoda pozwala głównej pętli programu sprawdzić czy
        może bezpiecznie dodać więcej danych do nagrania.
        """
        return self.is_available

    def data_info(self, version='1.0.0', date=None, author=None):
        """
        Przygotowuje metadane opisujące nagrane dane.
        
        Args:
            version (str): Wersja formatu danych
            date (str): Data nagrania
            author (str): Kto nagrał dane
            
        Dla początkujących:
        Metadane to "dane o danych" - informacje opisujące
        co zostało nagrane, kiedy, przez kogo, w jakim formacie.
        Są zapisywane w pliku JSON dla łatwego odczytu.
        """
        self.info = {
                "version": "1.0.0" if version is None else version, 
                "date": datetime.date.today().strftime('%Y-%m-%d') if date is None else date,
                "author": "unitree" if author is None else author,
                # Parametry obrazów
                "image": {"width":self.image_size[0], "height":self.image_size[1], "fps":self.frequency},
                # Parametry głębi (dla kamer 3D)
                "depth": {"width":self.image_size[0], "height":self.image_size[1], "fps":self.frequency},
                # Parametry audio (jeśli nagrywamy dźwięk)
                "audio": {"sample_rate": 16000, "channels": 1, "format":"PCM", "bits":16},    # PCM_S16
                # Nazwy stawów (zostaną wypełnione później)
                "joint_names":{
                    "left_arm":   [],  # Stawy lewego ramienia
                    "left_ee":  [],    # End-effector lewej ręki (dłoń)
                    "right_arm":  [],  # Stawy prawego ramienia
                    "right_ee": [],    # End-effector prawej ręki (dłoń)
                    "body":       [],  # Stawy korpusu (talia, głowa)
                },

                "tactile_names": {
                    "left_ee": [],
                    "right_ee": [],
                }, 
                "sim_state": ""
            }

 
    def create_episode(self):
        """
        Create a new episode.
        Returns:
            bool: True if the episode is successfully created, False otherwise.
        Note:
            Once successfully created, this function will only be available again after save_episode complete its save task.
        """
        if not self.is_available:
            logger_mp.info("==> The class is currently unavailable for new operations. Please wait until ongoing tasks are completed.")
            return False  # Return False if the class is unavailable

        # Reset episode-related data and create necessary directories
        self.item_id = -1
        self.episode_id = self.episode_id + 1
        
        self.episode_dir = os.path.join(self.task_dir, f"episode_{str(self.episode_id).zfill(4)}")
        self.color_dir = os.path.join(self.episode_dir, 'colors')
        self.depth_dir = os.path.join(self.episode_dir, 'depths')
        self.audio_dir = os.path.join(self.episode_dir, 'audios')
        self.json_path = os.path.join(self.episode_dir, 'data.json')
        os.makedirs(self.episode_dir, exist_ok=True)
        os.makedirs(self.color_dir, exist_ok=True)
        os.makedirs(self.depth_dir, exist_ok=True)
        os.makedirs(self.audio_dir, exist_ok=True)
        with open(self.json_path, "w", encoding="utf-8") as f:
            f.write('{\n')
            f.write('"info": ' + json.dumps(self.info, ensure_ascii=False, indent=4) + ',\n')
            f.write('"text": ' + json.dumps(self.text, ensure_ascii=False, indent=4) + ',\n')
            f.write('"data": [\n')
        self.first_item = True   # Flag to handle commas in JSON array

        if self.rerun_log:
            self.online_logger = RerunLogger(prefix="online/", IdxRangeBoundary = 60, memory_limit="300MB")

        self.is_available = False  # After the episode is created, the class is marked as unavailable until the episode is successfully saved
        logger_mp.info(f"==> New episode created: {self.episode_dir}")
        return True  # Return True if the episode is successfully created
        
    def add_item(self, colors, depths=None, states=None, actions=None, tactiles=None, audios=None, sim_state=None):
        # Increment the item ID
        self.item_id += 1
        # Create the item data dictionary
        item_data = {
            'idx': self.item_id,
            'colors': colors,
            'depths': depths,
            'states': states,
            'actions': actions,
            'tactiles': tactiles,
            'audios': audios,
            'sim_state': sim_state,
        }
        # Enqueue the item data
        self.item_data_queue.put(item_data)

    def process_queue(self):
        while not self.stop_worker or not self.item_data_queue.empty():
            # Process items in the queue
            try:
                item_data = self.item_data_queue.get(timeout=1)
                try:
                    self._process_item_data(item_data)
                except Exception as e:
                    logger_mp.info(f"Error processing item_data (idx={item_data['idx']}): {e}")
                self.item_data_queue.task_done()
            except Empty:
                pass
        
            # Check if save_episode was triggered
            if self.need_save and self.item_data_queue.empty():
                self._save_episode()

    def _process_item_data(self, item_data):
        idx = item_data['idx']
        colors = item_data.get('colors', {})
        depths = item_data.get('depths', {})
        audios = item_data.get('audios', {})

        # Save images
        if colors:
            for idx_color, (color_key, color) in enumerate(colors.items()):
                color_name = f'{str(idx).zfill(6)}_{color_key}.jpg'
                if not cv2.imwrite(os.path.join(self.color_dir, color_name), color):
                    logger_mp.info(f"Failed to save color image.")
                item_data['colors'][color_key] = os.path.join('colors', color_name)

        # Save depths
        if depths:
            for idx_depth, (depth_key, depth) in enumerate(depths.items()):
                depth_name = f'{str(idx).zfill(6)}_{depth_key}.jpg'
                if not cv2.imwrite(os.path.join(self.depth_dir, depth_name), depth):
                    logger_mp.info(f"Failed to save depth image.")
                item_data['depths'][depth_key] = os.path.join('depths', depth_name)

        # Save audios
        if audios:
            for mic, audio in audios.items():
                audio_name = f'audio_{str(idx).zfill(6)}_{mic}.npy'
                np.save(os.path.join(self.audio_dir, audio_name), audio.astype(np.int16))
                item_data['audios'][mic] = os.path.join('audios', audio_name)

        # Update episode data
        with open(self.json_path, "a", encoding="utf-8") as f:
            if not self.first_item:
                f.write(",\n")
            f.write(json.dumps(item_data, ensure_ascii=False, indent=4))
            self.first_item = False

        # Log data if necessary
        if self.rerun_log:
            curent_record_time = time.time()
            logger_mp.info(f"==> episode_id:{self.episode_id}  item_id:{idx}  current_time:{curent_record_time}")
            self.rerun_logger.log_item_data(item_data)

    def save_episode(self):
        """
        Trigger the save operation. This sets the save flag, and the process_queue thread will handle it.
        """
        self.need_save = True  # Set the save flag
        logger_mp.info(f"==> Episode saved start...")

    def _save_episode(self):
        """
        Save the episode data to a JSON file.
        """
        with open(self.json_path, "a", encoding="utf-8") as f:
            f.write("\n]\n}")      # Close the JSON array and object

        self.need_save = False     # Reset the save flag
        self.is_available = True   # Mark the class as available after saving
        logger_mp.info(f"==> Episode saved successfully to {self.json_path}.")

    def close(self):
        """
        Stop the worker thread and ensure all tasks are completed.
        """
        self.item_data_queue.join()
        if not self.is_available:  # If self.is_available is False, it means there is still data not saved.
            self.save_episode()
        while not self.is_available:
            time.sleep(0.01)
        self.stop_worker = True
        self.worker_thread.join()