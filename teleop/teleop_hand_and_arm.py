"""
teleop_hand_and_arm.py - Główny skrypt uruchomieniowy dla systemu teleoperation
=================================================================================

Ten plik zawiera główną logikę programu do zdalnego sterowania robotem humanoidalnym 
za pomocą urządzeń XR (gogle VR/AR).

CO ROBI TEN PROGRAM:
1. Inicjalizuje połączenie z robotem (przez DDS)
2. Łączy się z urządzeniem XR (przez televuer)
3. Odbiera dane ruchu z XR (pozycje dłoni, kontrolerów)
4. Przetwarza je na komendy dla robota (kinematyka odwrotna)
5. Wysyła komendy do robota w czasie rzeczywistym
6. Opcjonalnie nagrywa dane do późniejszego użycia (uczenie maszynowe)

DLA POCZĄTKUJĄCYCH:
- DDS = Data Distribution Service - protokół komunikacji między programami
- XR = Extended Reality - gogle VR/AR
- IK = Inverse Kinematics - obliczanie kątów stawów z pozycji docelowej
- Teleoperation = zdalne sterowanie robotem w czasie rzeczywistym
"""

# === IMPORT BIBLIOTEK PODSTAWOWYCH ===
import time           # Do pomiaru czasu i opóźnień
import argparse       # Do parsowania argumentów wiersza poleceń (--sim, --record, etc.)
from multiprocessing import Value, Array, Lock  # Do współdzielenia danych między procesami
import threading      # Do uruchamiania zadań równoległych
import logging_mp     # Biblioteka do logowania w środowisku wieloprocesowym
logging_mp.basic_config(level=logging_mp.INFO)  # Konfiguracja poziomu logowania (INFO = podstawowe informacje)
logger_mp = logging_mp.get_logger(__name__)     # Tworzy logger dla tego modułu

# === KONFIGURACJA ŚCIEŻEK ===
# Python potrzebuje wiedzieć gdzie szukać innych modułów projektu
import os 
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))  # Katalog tego pliku
parent_dir = os.path.dirname(current_dir)                  # Katalog nadrzędny
sys.path.append(parent_dir)  # Dodaj katalog nadrzędny do ścieżki wyszukiwania modułów

# === IMPORT BIBLIOTEK PROJEKTU ===
# Komunikacja z robotem
from unitree_sdk2py.core.channel import ChannelFactoryInitialize  # Inicjalizacja DDS (komunikacja z robotem)

# Interfejs XR (gogle VR/AR)
from televuer import TeleVuerWrapper  # Obsługa połączenia z goglami XR i śledzenia ruchów

# Sterowanie ramieniem robota
from teleop.robot_control.robot_arm import G1_29_ArmController, G1_23_ArmController, H1_2_ArmController, H1_ArmController
# Te kontrolery wysyłają komendy do motorów ramion różnych modeli robotów

# Kinematyka odwrotna (IK) ramienia
from teleop.robot_control.robot_arm_ik import G1_29_ArmIK, G1_23_ArmIK, H1_2_ArmIK, H1_ArmIK
# IK = Inverse Kinematics - oblicza jakie kąty stawów potrzebne są aby ramię osiągnęło żądaną pozycję

# Obsługa obrazu z kamer
from teleimager.image_client import ImageClient  # Klient do odbierania strumieni wideo z kamer robota

# Narzędzia pomocnicze
from teleop.utils.episode_writer import EpisodeWriter     # Zapisuje dane nagrań do plików
from teleop.utils.ipc import IPC_Server                   # Komunikacja międzyprocesowa (sterowanie z innych programów)
from teleop.utils.motion_switcher import MotionSwitcher, LocoClientWrapper  # Przełączanie trybów ruchu robota
from sshkeyboard import listen_keyboard, stop_listening   # Nasłuchiwanie klawiszy klawiatury (r, q, s)

# === FUNKCJE DO SYMULACJI ===
from unitree_sdk2py.core.channel import ChannelPublisher
from unitree_sdk2py.idl.std_msgs.msg.dds_ import String_

def publish_reset_category(category: int, publisher):
    """
    Publikuje sygnał resetowania sceny w symulacji.
    
    Args:
        category (int): Kategoria resetu (różne typy resetowania sceny)
        publisher: Wydawca DDS do wysyłania wiadomości
        
    Dla początkujących:
    Ta funkcja jest używana tylko w symulacji aby zresetować środowisko
    (np. przywrócić obiekty do pozycji początkowych)
    """
    msg = String_(data=str(category))  # Tworzy wiadomość ze stringiem
    publisher.Write(msg)               # Publikuje wiadomość przez DDS
    logger_mp.info(f"published reset category: {category}")

# === ZMIENNE GLOBALNE DLA MASZYNY STANÓW ===
# Te zmienne kontrolują stan programu (czy robot jest aktywny, czy nagrywamy, etc.)

START          = False  # Włącz aby robot zaczął śledzić ruchy użytkownika VR
STOP           = False  # Włącz aby rozpocząć procedurę zamykania systemu
READY          = False  # Gotowy do (1) wejścia w stan START, (2) wejścia w stan RECORD_RUNNING
RECORD_RUNNING = False  # True jeśli [Nagrywanie] jest aktywne
RECORD_TOGGLE  = False  # Przełącz stan nagrywania

# === DIAGRAM PRZEJŚĆ STANÓW ===
# Pokazuje jak program przechodzi między różnymi stanami:
#
#  -------        ---------                -----------                -----------            ---------
#   Stan           [Gotowy]      ==>        [Nagrywanie]    ==>         [AutoZapis]    -->     [Gotowy]
#  -------        ---------      |         -----------      |         -----------      |     ---------
#   START           True         |ręcznie     True          |ręcznie     True          |        True
#   READY           True         |ustaw       False         |ustaw       False         |auto    True
#   RECORD_RUNNING  False        |na          True          |na          False         |        False
#                                ∨                          ∨                          ∨
#   RECORD_TOGGLE   False       True          False        True          False                  False
#  -------        ---------                -----------                 -----------            ---------
#  
#  ==> ręcznie (manual): gdy READY jest True, ustaw RECORD_TOGGLE=True aby przejść do następnego stanu.
#  --> auto: Automatyczne przejście po zapisaniu danych.
#
# DLA POCZĄTKUJĄCYCH - Jak używać:
# 1. Uruchom program - stan to [Gotowy]
# 2. Naciśnij 'r' - robot zaczyna śledzić Twoje ruchy
# 3. Naciśnij 's' - rozpoczyna nagrywanie (stan [Nagrywanie])
# 4. Naciśnij 's' ponownie - zatrzymuje i zapisuje (stan [AutoZapis], potem wraca do [Gotowy])
# 5. Naciśnij 'q' - zamyka program

def on_press(key):
    """
    Funkcja wywoływana gdy użytkownik naciśnie klawisz na klawiaturze.
    
    Args:
        key (str): Naciśnięty klawisz ('r', 'q', 's', etc.)
        
    Obsługiwane klawisze:
    - 'r' (run)    : Rozpocznij teleoperation - robot zaczyna śledzić Twoje ruchy
    - 'q' (quit)   : Zakończ program i bezpiecznie zamknij połączenia
    - 's' (save)   : Przełącz nagrywanie (start/stop)
    
    Dla początkujących:
    global - słowo kluczowe pozwalające modyfikować zmienne globalne
    """
    global STOP, START, RECORD_TOGGLE
    if key == 'r':
        START = True  # Rozpocznij teleoperation
    elif key == 'q':
        START = False  # Zatrzymaj teleoperation
        STOP = True    # Rozpocznij procedurę zamykania
    elif key == 's' and START == True:
        RECORD_TOGGLE = True  # Przełącz stan nagrywania
    else:
        logger_mp.warning(f"[on_press] Naciśnięto {key}, ale nie zdefiniowano akcji dla tego klawisza.")

def get_state() -> dict:
    """
    Zwraca aktualny stan systemu jako słownik.
    
    Returns:
        dict: Słownik ze stanami:
              - START: Czy teleoperation jest aktywna
              - STOP: Czy rozpoczęto procedurę zamykania
              - READY: Czy system jest gotowy do nagrywania
              - RECORD_RUNNING: Czy nagrywanie jest aktywne
              
    Dla początkujących:
    Ta funkcja jest używana przez inne moduły (np. IPC) do sprawdzenia
    w jakim stanie znajduje się obecnie program.
    """
    global START, STOP, RECORD_RUNNING, READY
    return {
        "START": START,
        "STOP": STOP,
        "READY": READY,
        "RECORD_RUNNING": RECORD_RUNNING,
    }

# === GŁÓWNA FUNKCJA PROGRAMU ===
if __name__ == '__main__':
    # === KONFIGURACJA ARGUMENTÓW WIERSZA POLECEŃ ===
    # ArgumentParser pozwala użytkownikom przekazywać opcje przy uruchamianiu programu
    # Przykład: python teleop_hand_and_arm.py --sim --ee=dex3 --record
    parser = argparse.ArgumentParser()
    
    # --- Podstawowe parametry sterowania ---
    parser.add_argument('--frequency', type = float, default = 30.0, 
                        help = 'Częstotliwość sterowania i nagrywania w Hz (klatek na sekundę). '
                               'Określa jak często robot aktualizuje swoją pozycję. Domyślnie 30 Hz.')
    
    parser.add_argument('--input-mode', type=str, choices=['hand', 'controller'], default='hand', 
                        help='Wybierz źródło śledzenia wejścia urządzenia XR:\n'
                             '  hand - śledź pozycje dłoni użytkownika (wymaga wsparcia hand tracking)\n'
                             '  controller - śledź kontrolery VR')
    
    parser.add_argument('--display-mode', type=str, choices=['immersive', 'ego', 'pass-through'], default='immersive', 
                        help='Wybierz tryb wyświetlania XR:\n'
                             '  immersive - pełna immersja, widzisz tylko obraz z robota\n'
                             '  ego - widok pass-through + małe okno pierwszej osoby\n'
                             '  pass-through - tylko widok pass-through (zobacz otoczenie)')
    
    parser.add_argument('--arm', type=str, choices=['G1_29', 'G1_23', 'H1_2', 'H1'], default='G1_29', 
                        help='Wybierz kontroler ramienia:\n'
                             '  G1_29 - Robot G1 z 29 stopniami swobody\n'
                             '  G1_23 - Robot G1 z 23 stopniami swobody\n'
                             '  H1_2  - Robot H1 z ramieniem 7-DoF\n'
                             '  H1    - Robot H1 z ramieniem 4-DoF')
    
    parser.add_argument('--ee', type=str, choices=['dex1', 'dex3', 'inspire_ftp', 'inspire_dfx', 'brainco'], 
                        help='Wybierz kontroler efektora końcowego (dłoń/chwytak):\n'
                             '  dex1        - Chwytaki Unitree Dex1-1\n'
                             '  dex3        - Dłonie zręcznościowe Unitree Dex3-1\n'
                             '  inspire_ftp - Dłonie zręcznościowe Inspire FTP\n'
                             '  inspire_dfx - Dłonie zręcznościowe Inspire DFX\n'
                             '  brainco     - Dłonie zręcznościowe BrainCo')
    
    parser.add_argument('--img-server-ip', type=str, default='192.168.123.164', 
                        help='Adres IP serwera obrazu (PC2 robota lub komputer z symulacją). '
                             'Używany przez teleimager i televuer do przesyłania wideo. '
                             'Domyślnie: 192.168.123.164')
    
    parser.add_argument('--network-interface', type=str, default=None, 
                        help='Interfejs sieciowy dla komunikacji DDS (np. eth0, wlan0). '
                             'Jeśli None, użyje domyślnego interfejsu. '
                             'Przydatne gdy komputer ma wiele kart sieciowych.')
    
    # --- Flagi trybów ---
    parser.add_argument('--motion', action = 'store_true', 
                        help = 'Włącz tryb sterowania ruchem. '
                               'Program może działać równolegle z programem sterowania ruchem robota. '
                               'Robot może chodzić podczas gdy sterujesz ramionami.')
    
    parser.add_argument('--headless', action='store_true', 
                        help='Włącz tryb bezgłowy (bez wyświetlacza). '
                             'Do uruchamiania na urządzeniach bez monitora, np. PC2.')
    
    parser.add_argument('--sim', action = 'store_true', 
                        help = 'Włącz tryb symulacji Isaac. '
                               'Łączy się z symulatorem zamiast fizycznego robota. '
                               'Bezpieczne dla testowania bez sprzętu.')
    
    parser.add_argument('--ipc', action = 'store_true', 
                        help = 'Włącz serwer IPC do obsługi wejścia; w przeciwnym razie użyj sshkeyboard. '
                               'IPC pozwala sterować programem z innych procesów.')
    
    parser.add_argument('--affinity', action = 'store_true', 
                        help = 'Włącz wysoki priorytet i ustaw tryb powinowactwa CPU. '
                               'Rezerwuje rdzenie CPU dla tego programu (zaawansowane).')
    
    # --- Tryb nagrywania i informacje o zadaniu ---
    parser.add_argument('--record', action = 'store_true', 
                        help = 'Włącz tryb nagrywania danych. '
                               'Naciśnij "s" aby rozpocząć/zatrzymać nagrywanie.')
    
    parser.add_argument('--task-dir', type = str, default = './utils/data/', 
                        help = 'Ścieżka zapisu danych nagrań')
    
    parser.add_argument('--task-name', type = str, default = 'pick cube', 
                        help = 'Nazwa pliku zadania dla nagrania')
    
    parser.add_argument('--task-goal', type = str, default = 'pick up cube.', 
                        help = 'Cel zadania do zapisania w pliku JSON')
    
    parser.add_argument('--task-desc', type = str, default = 'task description', 
                        help = 'Opis zadania do zapisania w pliku JSON')
    
    parser.add_argument('--task-steps', type = str, default = 'step1: do this; step2: do that;', 
                        help = 'Kroki zadania do zapisania w pliku JSON')

    # Parsuj argumenty przekazane przez użytkownika
    args = parser.parse_args()
    logger_mp.info(f"Argumenty programu: {args}")

    try:
        # setup dds communication domains id
        if args.sim:
            ChannelFactoryInitialize(1, networkInterface=args.network_interface)
        else:
            ChannelFactoryInitialize(0, networkInterface=args.network_interface)

        # ipc communication mode. client usage: see utils/ipc.py
        if args.ipc:
            ipc_server = IPC_Server(on_press=on_press,get_state=get_state)
            ipc_server.start()
        # sshkeyboard communication mode
        else:
            listen_keyboard_thread = threading.Thread(target=listen_keyboard, 
                                                      kwargs={"on_press": on_press, "until": None, "sequential": False,}, 
                                                      daemon=True)
            listen_keyboard_thread.start()

        # image client
        img_client = ImageClient(host=args.img_server_ip)
        camera_config = img_client.get_cam_config()
        logger_mp.debug(f"Camera config: {camera_config}")
        xr_need_local_img = not (args.display_mode == 'pass-through' or camera_config['head_camera']['enable_webrtc'])

        # televuer_wrapper: obtain hand pose data from the XR device and transmit the robot's head camera image to the XR device.
        tv_wrapper = TeleVuerWrapper(use_hand_tracking=args.input_mode == "hand", 
                                     binocular=camera_config['head_camera']['binocular'],
                                     img_shape=camera_config['head_camera']['image_shape'],
                                     # maybe should decrease fps for better performance?
                                     # https://github.com/unitreerobotics/xr_teleoperate/issues/172
                                     # display_fps=camera_config['head_camera']['fps'] ? args.frequency? 30.0?
                                     display_mode=args.display_mode,
                                     zmq=camera_config['head_camera']['enable_zmq'],
                                     webrtc=camera_config['head_camera']['enable_webrtc'],
                                     webrtc_url=f"https://{args.img_server_ip}:{camera_config['head_camera']['webrtc_port']}/offer",
                                     )
        
        # motion mode (G1: Regular mode R1+X, not Running mode R2+A)
        if args.motion:
            if args.input_mode == "controller":
                loco_wrapper = LocoClientWrapper()
        else:
            motion_switcher = MotionSwitcher()
            status, result = motion_switcher.Enter_Debug_Mode()
            logger_mp.info(f"Enter debug mode: {'Success' if status == 0 else 'Failed'}")

        # arm
        if args.arm == "G1_29":
            arm_ik = G1_29_ArmIK()
            arm_ctrl = G1_29_ArmController(motion_mode=args.motion, simulation_mode=args.sim)
        elif args.arm == "G1_23":
            arm_ik = G1_23_ArmIK()
            arm_ctrl = G1_23_ArmController(motion_mode=args.motion, simulation_mode=args.sim)
        elif args.arm == "H1_2":
            arm_ik = H1_2_ArmIK()
            arm_ctrl = H1_2_ArmController(motion_mode=args.motion, simulation_mode=args.sim)
        elif args.arm == "H1":
            arm_ik = H1_ArmIK()
            arm_ctrl = H1_ArmController(simulation_mode=args.sim)

        # end-effector
        if args.ee == "dex3":
            from teleop.robot_control.robot_hand_unitree import Dex3_1_Controller
            left_hand_pos_array = Array('d', 75, lock = True)      # [input]
            right_hand_pos_array = Array('d', 75, lock = True)     # [input]
            dual_hand_data_lock = Lock()
            dual_hand_state_array = Array('d', 14, lock = False)   # [output] current left, right hand state(14) data.
            dual_hand_action_array = Array('d', 14, lock = False)  # [output] current left, right hand action(14) data.
            hand_ctrl = Dex3_1_Controller(left_hand_pos_array, right_hand_pos_array, dual_hand_data_lock, 
                                          dual_hand_state_array, dual_hand_action_array, simulation_mode=args.sim)
        elif args.ee == "dex1":
            from teleop.robot_control.robot_hand_unitree import Dex1_1_Gripper_Controller
            left_gripper_value = Value('d', 0.0, lock=True)        # [input]
            right_gripper_value = Value('d', 0.0, lock=True)       # [input]
            dual_gripper_data_lock = Lock()
            dual_gripper_state_array = Array('d', 2, lock=False)   # current left, right gripper state(2) data.
            dual_gripper_action_array = Array('d', 2, lock=False)  # current left, right gripper action(2) data.
            gripper_ctrl = Dex1_1_Gripper_Controller(left_gripper_value, right_gripper_value, dual_gripper_data_lock, 
                                                     dual_gripper_state_array, dual_gripper_action_array, simulation_mode=args.sim)
        elif args.ee == "inspire_dfx":
            from teleop.robot_control.robot_hand_inspire import Inspire_Controller_DFX
            left_hand_pos_array = Array('d', 75, lock = True)      # [input]
            right_hand_pos_array = Array('d', 75, lock = True)     # [input]
            dual_hand_data_lock = Lock()
            dual_hand_state_array = Array('d', 12, lock = False)   # [output] current left, right hand state(12) data.
            dual_hand_action_array = Array('d', 12, lock = False)  # [output] current left, right hand action(12) data.
            hand_ctrl = Inspire_Controller_DFX(left_hand_pos_array, right_hand_pos_array, dual_hand_data_lock, dual_hand_state_array, dual_hand_action_array, simulation_mode=args.sim)
        elif args.ee == "inspire_ftp":
            from teleop.robot_control.robot_hand_inspire import Inspire_Controller_FTP
            left_hand_pos_array = Array('d', 75, lock = True)      # [input]
            right_hand_pos_array = Array('d', 75, lock = True)     # [input]
            dual_hand_data_lock = Lock()
            dual_hand_state_array = Array('d', 12, lock = False)   # [output] current left, right hand state(12) data.
            dual_hand_action_array = Array('d', 12, lock = False)  # [output] current left, right hand action(12) data.
            hand_ctrl = Inspire_Controller_FTP(left_hand_pos_array, right_hand_pos_array, dual_hand_data_lock, dual_hand_state_array, dual_hand_action_array, simulation_mode=args.sim)
        elif args.ee == "brainco":
            from teleop.robot_control.robot_hand_brainco import Brainco_Controller
            left_hand_pos_array = Array('d', 75, lock = True)      # [input]
            right_hand_pos_array = Array('d', 75, lock = True)     # [input]
            dual_hand_data_lock = Lock()
            dual_hand_state_array = Array('d', 12, lock = False)   # [output] current left, right hand state(12) data.
            dual_hand_action_array = Array('d', 12, lock = False)  # [output] current left, right hand action(12) data.
            hand_ctrl = Brainco_Controller(left_hand_pos_array, right_hand_pos_array, dual_hand_data_lock, 
                                           dual_hand_state_array, dual_hand_action_array, simulation_mode=args.sim)
        else:
            pass
        
        # affinity mode (if you dont know what it is, then you probably don't need it)
        if args.affinity:
            import psutil
            p = psutil.Process(os.getpid())
            p.cpu_affinity([0,1,2,3]) # Set CPU affinity to cores 0-3
            try:
                p.nice(-20)           # Set highest priority
                logger_mp.info("Set high priority successfully.")
            except psutil.AccessDenied:
                logger_mp.warning("Failed to set high priority. Please run as root.")
                
            for child in p.children(recursive=True):
                try:
                    logger_mp.info(f"Child process {child.pid} name: {child.name()}")
                    child.cpu_affinity([5,6])
                    child.nice(-20)
                except psutil.AccessDenied:
                    pass

        # simulation mode
        if args.sim:
            reset_pose_publisher = ChannelPublisher("rt/reset_pose/cmd", String_)
            reset_pose_publisher.Init()
            from teleop.utils.sim_state_topic import start_sim_state_subscribe
            sim_state_subscriber = start_sim_state_subscribe()

        # record + headless / non-headless mode
        if args.record:
            recorder = EpisodeWriter(task_dir = os.path.join(args.task_dir, args.task_name),
                                     task_goal = args.task_goal,
                                     task_desc = args.task_desc,
                                     task_steps = args.task_steps,
                                     frequency = args.frequency, 
                                     rerun_log = not args.headless)

        logger_mp.info("----------------------------------------------------------------")
        logger_mp.info("🟢  Press [r] to start syncing the robot with your movements.")
        if args.record:
            logger_mp.info("🟡  Press [s] to START or SAVE recording (toggle cycle).")
        else:
            logger_mp.info("🔵  Recording is DISABLED (run with --record to enable).")
        logger_mp.info("🔴  Press [q] to stop and exit the program.")
        logger_mp.info("⚠️  IMPORTANT: Please keep your distance and stay safe.")
        READY = True                  # now ready to (1) enter START state
        while not START and not STOP: # wait for start or stop signal.
            time.sleep(0.033)
            if camera_config['head_camera']['enable_zmq'] and xr_need_local_img:
                head_img, _ = img_client.get_head_frame()
                tv_wrapper.render_to_xr(head_img)

        logger_mp.info("---------------------🚀start Tracking🚀-------------------------")
        arm_ctrl.speed_gradual_max()
        # main loop. robot start to follow VR user's motion
        while not STOP:
            start_time = time.time()
            # get image
            if camera_config['head_camera']['enable_zmq']:
                if args.record or xr_need_local_img:
                    head_img, head_img_fps = img_client.get_head_frame()
                if xr_need_local_img:
                    tv_wrapper.render_to_xr(head_img)
            if camera_config['left_wrist_camera']['enable_zmq']:
                if args.record:
                    left_wrist_img, _ = img_client.get_left_wrist_frame()
            if camera_config['right_wrist_camera']['enable_zmq']:
                if args.record:
                    right_wrist_img, _ = img_client.get_right_wrist_frame()

            # record mode
            if args.record and RECORD_TOGGLE:
                RECORD_TOGGLE = False
                if not RECORD_RUNNING:
                    if recorder.create_episode():
                        RECORD_RUNNING = True
                    else:
                        logger_mp.error("Failed to create episode. Recording not started.")
                else:
                    RECORD_RUNNING = False
                    recorder.save_episode()
                    if args.sim:
                        publish_reset_category(1, reset_pose_publisher)

            # get xr's tele data
            tele_data = tv_wrapper.get_tele_data()
            if (args.ee == "dex3" or args.ee == "inspire_dfx" or args.ee == "inspire_ftp" or args.ee == "brainco") and args.input_mode == "hand":
                with left_hand_pos_array.get_lock():
                    left_hand_pos_array[:] = tele_data.left_hand_pos.flatten()
                with right_hand_pos_array.get_lock():
                    right_hand_pos_array[:] = tele_data.right_hand_pos.flatten()
            elif args.ee == "dex1" and args.input_mode == "controller":
                with left_gripper_value.get_lock():
                    left_gripper_value.value = tele_data.left_ctrl_triggerValue
                with right_gripper_value.get_lock():
                    right_gripper_value.value = tele_data.right_ctrl_triggerValue
            elif args.ee == "dex1" and args.input_mode == "hand":
                with left_gripper_value.get_lock():
                    left_gripper_value.value = tele_data.left_hand_pinchValue
                with right_gripper_value.get_lock():
                    right_gripper_value.value = tele_data.right_hand_pinchValue
            else:
                pass
            
            # high level control
            if args.input_mode == "controller" and args.motion:
                # quit teleoperate
                if tele_data.right_ctrl_aButton:
                    START = False
                    STOP = True
                # command robot to enter damping mode. soft emergency stop function
                if tele_data.left_ctrl_thumbstick and tele_data.right_ctrl_thumbstick:
                    loco_wrapper.Damp()
                # https://github.com/unitreerobotics/xr_teleoperate/issues/135, control, limit velocity to within 0.3
                loco_wrapper.Move(-tele_data.left_ctrl_thumbstickValue[1] * 0.3,
                                  -tele_data.left_ctrl_thumbstickValue[0] * 0.3,
                                  -tele_data.right_ctrl_thumbstickValue[0]* 0.3)

            # get current robot state data.
            current_lr_arm_q  = arm_ctrl.get_current_dual_arm_q()
            current_lr_arm_dq = arm_ctrl.get_current_dual_arm_dq()

            # solve ik using motor data and wrist pose, then use ik results to control arms.
            time_ik_start = time.time()
            sol_q, sol_tauff  = arm_ik.solve_ik(tele_data.left_wrist_pose, tele_data.right_wrist_pose, current_lr_arm_q, current_lr_arm_dq)
            time_ik_end = time.time()
            logger_mp.debug(f"ik:\t{round(time_ik_end - time_ik_start, 6)}")
            arm_ctrl.ctrl_dual_arm(sol_q, sol_tauff)

            # record data
            if args.record:
                READY = recorder.is_ready() # now ready to (2) enter RECORD_RUNNING state
                # dex hand or gripper
                if args.ee == "dex3" and args.input_mode == "hand":
                    with dual_hand_data_lock:
                        left_ee_state = dual_hand_state_array[:7]
                        right_ee_state = dual_hand_state_array[-7:]
                        left_hand_action = dual_hand_action_array[:7]
                        right_hand_action = dual_hand_action_array[-7:]
                        current_body_state = []
                        current_body_action = []
                elif args.ee == "dex1" and args.input_mode == "hand":
                    with dual_gripper_data_lock:
                        left_ee_state = [dual_gripper_state_array[0]]
                        right_ee_state = [dual_gripper_state_array[1]]
                        left_hand_action = [dual_gripper_action_array[0]]
                        right_hand_action = [dual_gripper_action_array[1]]
                        current_body_state = []
                        current_body_action = []
                elif args.ee == "dex1" and args.input_mode == "controller":
                    with dual_gripper_data_lock:
                        left_ee_state = [dual_gripper_state_array[0]]
                        right_ee_state = [dual_gripper_state_array[1]]
                        left_hand_action = [dual_gripper_action_array[0]]
                        right_hand_action = [dual_gripper_action_array[1]]
                        current_body_state = arm_ctrl.get_current_motor_q().tolist()
                        current_body_action = [-tele_data.left_ctrl_thumbstickValue[1]  * 0.3,
                                               -tele_data.left_ctrl_thumbstickValue[0]  * 0.3,
                                               -tele_data.right_ctrl_thumbstickValue[0] * 0.3]
                elif (args.ee == "inspire_dfx" or args.ee == "inspire_ftp" or args.ee == "brainco") and args.input_mode == "hand":
                    with dual_hand_data_lock:
                        left_ee_state = dual_hand_state_array[:6]
                        right_ee_state = dual_hand_state_array[-6:]
                        left_hand_action = dual_hand_action_array[:6]
                        right_hand_action = dual_hand_action_array[-6:]
                        current_body_state = []
                        current_body_action = []
                else:
                    left_ee_state = []
                    right_ee_state = []
                    left_hand_action = []
                    right_hand_action = []
                    current_body_state = []
                    current_body_action = []

                # arm state and action
                left_arm_state  = current_lr_arm_q[:7]
                right_arm_state = current_lr_arm_q[-7:]
                left_arm_action = sol_q[:7]
                right_arm_action = sol_q[-7:]
                if RECORD_RUNNING:
                    colors = {}
                    depths = {}
                    if camera_config['head_camera']['binocular']:
                        if head_img is not None:
                            colors[f"color_{0}"] = head_img[:, :camera_config['head_camera']['image_shape'][1]//2]
                            colors[f"color_{1}"] = head_img[:, camera_config['head_camera']['image_shape'][1]//2:]
                        else:
                            logger_mp.warning("Head image is None!")
                        if camera_config['left_wrist_camera']['enable_zmq']:
                            if left_wrist_img is not None:
                                colors[f"color_{2}"] = left_wrist_img
                            else:
                                logger_mp.warning("Left wrist image is None!")
                        if camera_config['right_wrist_camera']['enable_zmq']:
                            if right_wrist_img is not None:
                                colors[f"color_{3}"] = right_wrist_img
                            else:
                                logger_mp.warning("Right wrist image is None!")
                    else:
                        if head_img is not None:
                            colors[f"color_{0}"] = head_img
                        else:
                            logger_mp.warning("Head image is None!")
                        if camera_config['left_wrist_camera']['enable_zmq']:
                            if left_wrist_img is not None:
                                colors[f"color_{1}"] = left_wrist_img
                            else:
                                logger_mp.warning("Left wrist image is None!")
                        if camera_config['right_wrist_camera']['enable_zmq']:
                            if right_wrist_img is not None:
                                colors[f"color_{2}"] = right_wrist_img
                            else:
                                logger_mp.warning("Right wrist image is None!")
                    states = {
                        "left_arm": {                                                                    
                            "qpos":   left_arm_state.tolist(),    # numpy.array -> list
                            "qvel":   [],                          
                            "torque": [],                        
                        }, 
                        "right_arm": {                                                                    
                            "qpos":   right_arm_state.tolist(),       
                            "qvel":   [],                          
                            "torque": [],                         
                        },                        
                        "left_ee": {                                                                    
                            "qpos":   left_ee_state,           
                            "qvel":   [],                           
                            "torque": [],                          
                        }, 
                        "right_ee": {                                                                    
                            "qpos":   right_ee_state,       
                            "qvel":   [],                           
                            "torque": [],  
                        }, 
                        "body": {
                            "qpos": current_body_state,
                        }, 
                    }
                    actions = {
                        "left_arm": {                                   
                            "qpos":   left_arm_action.tolist(),       
                            "qvel":   [],       
                            "torque": [],      
                        }, 
                        "right_arm": {                                   
                            "qpos":   right_arm_action.tolist(),       
                            "qvel":   [],       
                            "torque": [],       
                        },                         
                        "left_ee": {                                   
                            "qpos":   left_hand_action,       
                            "qvel":   [],       
                            "torque": [],       
                        }, 
                        "right_ee": {                                   
                            "qpos":   right_hand_action,       
                            "qvel":   [],       
                            "torque": [], 
                        }, 
                        "body": {
                            "qpos": current_body_action,
                        }, 
                    }
                    if args.sim:
                        sim_state = sim_state_subscriber.read_data()            
                        recorder.add_item(colors=colors, depths=depths, states=states, actions=actions, sim_state=sim_state)
                    else:
                        recorder.add_item(colors=colors, depths=depths, states=states, actions=actions)

            current_time = time.time()
            time_elapsed = current_time - start_time
            sleep_time = max(0, (1 / args.frequency) - time_elapsed)
            time.sleep(sleep_time)
            logger_mp.debug(f"main process sleep: {sleep_time}")

    except KeyboardInterrupt:
        logger_mp.info("⛔ KeyboardInterrupt, exiting program...")
    except Exception:
        import traceback
        logger_mp.error(traceback.format_exc())
    finally:
        try:
            arm_ctrl.ctrl_dual_arm_go_home()
        except Exception as e:
            logger_mp.error(f"Failed to ctrl_dual_arm_go_home: {e}")
        
        try:
            if args.ipc:
                ipc_server.stop()
            else:
                stop_listening()
                listen_keyboard_thread.join()
        except Exception as e:
            logger_mp.error(f"Failed to stop keyboard listener or ipc server: {e}")
        
        try:
            img_client.close()
        except Exception as e:
            logger_mp.error(f"Failed to close image client: {e}")

        try:
            tv_wrapper.close()
        except Exception as e:
            logger_mp.error(f"Failed to close televuer wrapper: {e}")

        try:
            if not args.motion:
                pass
                # status, result = motion_switcher.Exit_Debug_Mode()
                # logger_mp.info(f"Exit debug mode: {'Success' if status == 3104 else 'Failed'}")
        except Exception as e:
            logger_mp.error(f"Failed to exit debug mode: {e}")

        try:
            if args.sim:
                sim_state_subscriber.stop_subscribe()
        except Exception as e:
            logger_mp.error(f"Failed to stop sim state subscriber: {e}")
        
        try:
            if args.record:
                recorder.close()
        except Exception as e:
            logger_mp.error(f"Failed to close recorder: {e}")
        logger_mp.info("✅ Finally, exiting program.")
        exit(0)