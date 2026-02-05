# Przewodnik konfiguracji Meta Quest 3
## Sterowanie robotem Unitree za pomocą Meta Quest 3

Ten dokument opisuje specyficzne kroki konfiguracji wymagane do użycia Meta Quest 3 jako urządzenia sterującego dla robotów Unitree.

---

## 📋 Wymagania

### Sprzęt
- Meta Quest 3 z aktualnym oprogramowaniem układowym
- Kontrolery Quest 3 (2 sztuki) z naładowanymi bateriami
- Router WiFi (zalecany standard WiFi 6 lub nowszy)
- Komputer z Ubuntu 20.04/22.04
- Robot Unitree (G1, H1 lub H1_2)

### Oprogramowanie
Przed kontynuacją upewnij się, że zainstalowałeś:
- Środowisko `xr_teleoperate` (zobacz główny README)
- Bibliotekę `unitree_sdk2_python`
- Moduły `teleimager` i `televuer`

---

## 🔧 Część 1: Przygotowanie sieci

### Krok 1: Konfiguracja routera
1. Skonfiguruj dedykowaną sieć WiFi dla telepracy
2. Zalecane ustawienia:
   - Częstotliwość: 5GHz (mniejsze opóźnienia)
   - Kanał: Wybierz najmniej zajęty
   - Szerokość pasma: 80MHz lub więcej
   - Bezpieczeństwo: WPA3 lub WPA2

### Krok 2: Identyfikacja adresu IP komputera sterującego
```bash
ip addr show | grep "inet " | grep -v 127.0.0.1
```
Zanotuj adres IPv4, np. `192.168.1.100`

### Krok 3: Połączenie Quest 3 z siecią
1. W zestawie Quest 3, otwórz menu systemowe
2. Wybierz **Settings** > **WiFi**
3. Połącz się z siecią skonfigurowaną w Kroku 1
4. Zweryfikuj połączenie otwierając przeglądarkę i odwiedzając dowolną stronę

---

## 🔐 Część 2: Konfiguracja certyfikatów SSL

Meta Quest 3 wymaga certyfikatów SSL do bezpiecznego połączenia WebRTC.

### Generowanie certyfikatów

Przejdź do katalogu televuer:
```bash
cd ~/xr_teleoperate/teleop/televuer
```

Wygeneruj certyfikat samopodpisany:
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout quest3_key.pem -out quest3_cert.pem \
  -subj "/C=PL/ST=Mazowieckie/L=Warszawa/O=Teleoperacja/CN=quest3-server"
```

### Instalacja certyfikatów

Utwórz katalog konfiguracyjny:
```bash
mkdir -p ~/.config/xr_teleoperate/
cp quest3_cert.pem ~/.config/xr_teleoperate/cert.pem
cp quest3_key.pem ~/.config/xr_teleoperate/key.pem
```

Alternatywnie, użyj zmiennych środowiskowych:
```bash
echo 'export XR_TELEOP_CERT="$HOME/xr_teleoperate/teleop/televuer/quest3_cert.pem"' >> ~/.bashrc
echo 'export XR_TELEOP_KEY="$HOME/xr_teleoperate/teleop/televuer/quest3_key.pem"' >> ~/.bashrc
source ~/.bashrc
```

### Konfiguracja zapory sieciowej

Otwórz niezbędne porty:
```bash
sudo ufw allow 8012/tcp comment 'Vuer server dla Quest 3'
sudo ufw allow 60001/tcp comment 'Teleimager WebRTC dla Quest 3'
sudo ufw reload
```

Zweryfikuj reguły:
```bash
sudo ufw status numbered
```

---

## 🎮 Część 3: Wybór trybu sterowania

Meta Quest 3 obsługuje dwa tryby wejścia:

### Tryb A: Sterowanie kontrolerami (zalecane dla precyzji)
- Używa fizycznych kontrolerów Quest 3
- Lepsze śledzenie pozycji
- Mniejsze drżenie
- Przyciski do dodatkowych funkcji

### Tryb B: Śledzenie dłoni (zalecane dla naturalności)
- Bezpośrednie śledzenie ruchów dłoni
- Bardziej intuicyjne
- Wymaga dobrych warunków oświetleniowych
- Może być mniej stabilne przy szybkich ruchach

---

## 🚀 Część 4: Uruchomienie systemu

### Dla trybu kontrolerów:

```bash
cd ~/xr_teleoperate/teleop/

python teleop_hand_and_arm.py \
  --input-mode=controller \
  --arm=G1_29 \
  --ee=dex3 \
  --img-server-ip=ADRES_IP_PC2 \
  --frequency=30.0
```

### Dla trybu śledzenia dłoni:

```bash
python teleop_hand_and_arm.py \
  --input-mode=hand \
  --arm=G1_29 \
  --ee=dex3 \
  --img-server-ip=ADRES_IP_PC2 \
  --frequency=30.0
```

Zamień `ADRES_IP_PC2` na rzeczywisty adres IP jednostki PC2 robota (zazwyczaj `192.168.123.164`).

---

## 🥽 Część 5: Procedura połączenia Quest 3

### Krok 1: Uruchom usługę obrazu (jeśli używasz fizycznego robota)
Na jednostce PC2:
```bash
teleimager-server
```

### Krok 2: Uruchom główny program teleoperacji
Na komputerze sterującym:
```bash
cd ~/xr_teleoperate/teleop/
python teleop_hand_and_arm.py --input-mode=controller --arm=G1_29 --ee=dex3
```

### Krok 3: Połącz Quest 3 z interfejsem

1. Załóż zestaw Meta Quest 3
2. Upewnij się, że kontrolery są włączone i śledzone
3. Otwórz **Browser** z biblioteki aplikacji Quest
4. Wprowadź adres (zastąp `192.168.1.100` swoim IP hosta):
   ```
   https://192.168.1.100:8012/?ws=wss://192.168.1.100:8012
   ```

### Krok 4: Zaakceptuj certyfikat

1. Zobaczysz ostrzeżenie bezpieczeństwa
2. Dotknij **Advanced** (Zaawansowane)
3. Dotknij **Proceed** (Kontynuuj)
4. To jest normalne dla certyfikatów samopodpisanych

### Krok 5: Aktywuj sesję VR

1. Na stronie internetowej znajdź przycisk **"Virtual Reality"** lub **"Enter VR"**
2. Dotknij przycisku
3. Zaakceptuj wszystkie pozwolenia:
   - Dostęp do pozycji
   - Dostęp do orientacji
   - Dostęp do kontrolerów/dłoni

### Krok 6: Test połączenia WebRTC (jeśli używane)

Jeśli usługa obrazu używa WebRTC, najpierw przetestuj:
```
https://192.168.123.164:60001
```

1. Otwórz ten adres w przeglądarce Quest
2. Zaakceptuj certyfikat (jak wcześniej)
3. Dotknij przycisku **Start**
4. Powinieneś zobaczyć podgląd kamery robota
5. To potwierdza, że WebRTC działa poprawnie

### Krok 7: Inicjalizacja pozy

1. W środowisku VR zobaczysz wirtualny model robota
2. Ustaw swoje ramiona/kontrolery w pozycji odpowiadającej pozycji początkowej robota:
   - Ramiona wzdłuż ciała
   - Łokcie lekko zgięte
   - Dłonie przed sobą
3. Patrz na terminal komputera sterującego

### Krok 8: Aktywacja teleoperacji

W terminalu komputera naciśnij klawisz `r` (run), aby rozpocząć aktywną teleoperację.

### Krok 9: Sterowanie robotem

- Poruszaj kontrolerami/dłońmi - robot będzie naśladował ruchy
- Gesty chwytania - sterowanie efektorem końcowym
- W trybie kontrolera: przyciski mogą mieć dodatkowe funkcje

---

## ⚙️ Część 6: Dostrajanie wydajności

### Zmniejszenie opóźnień

Jeśli doświadczasz opóźnień, spróbuj:

```bash
python teleop_hand_and_arm.py \
  --input-mode=controller \
  --arm=G1_29 \
  --frequency=20.0 \
  --img-server-ip=192.168.123.164
```

Niższa częstotliwość (20 Hz zamiast 30 Hz) zmniejsza obciążenie sieci.

### Optymalizacja jakości obrazu

Edytuj `cam_config_server.yaml` na PC2:
```yaml
head_camera:
  enable_webrtc: true
  resolution: [1280, 720]  # Zmniejsz z 1920x1080 jeśli potrzeba
  fps: 30
  bitrate: 2000000  # 2 Mbps, dostosuj według potrzeb
```

### Priorytet procesów

Dla krytycznej wydajności:
```bash
sudo nice -n -10 python teleop_hand_and_arm.py --input-mode=controller --arm=G1_29
```

---

## 🔍 Część 7: Diagnozowanie problemów

### Problem: "Connection refused" przy łączeniu

**Możliwe przyczyny:**
- Firewall blokuje port 8012
- Nieprawidłowy adres IP
- Program teleoperacji nie działa

**Rozwiązanie:**
```bash
# Sprawdź czy program działa
ps aux | grep teleop_hand_and_arm

# Sprawdź czy port jest otwarty
sudo netstat -tulpn | grep 8012

# Sprawdź firewall
sudo ufw status

# Sprawdź adres IP
ip addr show
```

### Problem: "Certificate error" nie znika

**Rozwiązanie:**
1. Upewnij się, że wybierasz "Proceed" lub "Continue"
2. Niektóre przeglądarki Quest wymagają ręcznego potwierdzenia
3. Spróbuj wygenerować nowe certyfikaty z dłuższym okresem ważności (730 dni)

### Problem: Przerywane śledzenie kontrolerów

**Możliwe przyczyny:**
- Słabe oświetlenie
- Refleksje na lustrzanych powierzchniach
- Niski poziom baterii kontrolerów

**Rozwiązanie:**
1. Popraw oświetlenie w pomieszczeniu
2. Usuń lustra lub błyszczące powierzchnie
3. Wymień baterie w kontrolerach
4. Przedefiniuj granice gry w Quest

### Problem: Wysokie opóźnienie obrazu

**Rozwiązanie:**
1. Zmniejsz rozdzielczość kamery
2. Obniż częstotliwość do 20 Hz
3. Użyj połączenia kablowego Ethernet dla komputera sterującego
4. Zmniejsz odległość między Quest a routerem
5. Sprawdź użycie pasma przez inne urządzenia:
   ```bash
   iftop -i wlan0  # Zainstaluj przez: sudo apt install iftop
   ```

### Problem: Robot reaguje z opóźnieniem

**Diagnostyka:**
```bash
# Sprawdź opóźnienie sieci
ping 192.168.123.164

# Sprawdź obciążenie CPU
htop

# Sprawdź logi programu
# Terminal pokaże FPS i czasy przetwarzania
```

**Rozwiązanie:**
- Jeśli ping > 10ms: problem sieciowy
- Jeśli CPU > 90%: zbyt wiele procesów, zamknij niepotrzebne aplikacje
- Rozważ użycie `--affinity` do przypisania rdzeni CPU

### Problem: Śledzenie dłoni nie działa

**Wymagania dla śledzenia dłoni:**
1. Dobre, równomierne oświetlenie (> 300 lux)
2. Dłonie w polu widzenia kamer Quest
3. Brak rękawiczek ani naklejek na dłoniach
4. Włączone śledzenie dłoni w ustawieniach Quest

**Weryfikacja:**
1. Idź do **Settings** > **Hands and Controllers**
2. Upewnij się, że **Hand Tracking** jest włączone
3. Przetestuj śledzenie w środowisku głównym Quest

---

## 📊 Część 8: Parametry zaawansowane

### Wszystkie dostępne parametry dla Quest 3

```bash
python teleop_hand_and_arm.py \
  --input-mode=controller \        # lub 'hand'
  --display-mode=immersive \       # lub 'ego', 'pass-through'
  --arm=G1_29 \                    # Typ robota
  --ee=dex3 \                      # Typ efektora
  --frequency=30.0 \               # FPS sterowania
  --img-server-ip=192.168.123.164 \  # IP usługi obrazu
  --network-interface=eth0 \       # Interfejs sieciowy DDS
  --motion \                       # Tryb ruchu (opcjonalnie)
  --record \                       # Nagrywanie danych (opcjonalnie)
  --task-name="moja_praca" \       # Nazwa zadania (z --record)
  --task-description="Opis"        # Opis zadania (z --record)
```

### Tryb wyświetlania

- `immersive`: Pełne immersyjne VR (zalecane)
- `ego`: Pass-through + małe okno perspektywy robota
- `pass-through`: Tylko tryb pass-through

### Nagrywanie demonstracji

Aby nagrać dane treningowe:
```bash
python teleop_hand_and_arm.py \
  --input-mode=controller \
  --arm=G1_29 \
  --ee=dex3 \
  --record \
  --task-name="podnoszenie_obiektow" \
  --task-description="Robot podnosi i przenosi obiekty"
```

Podczas sesji:
- Naciśnij `r` - rozpocznij teleoperację
- Naciśnij `s` - rozpocznij nagrywanie epizodu
- Naciśnij `s` ponownie - zakończ i zapisz epizod
- Naciśnij `q` - zakończ program

Dane zostaną zapisane w `~/xr_teleoperate/teleop/utils/data/`

---

## 🛡️ Część 9: Bezpieczeństwo

### Środki ostrożności przy pracy z fizycznym robotem

⚠️ **BARDZO WAŻNE:**

1. **Zawsze utrzymuj bezpieczną odległość** (minimum 2 metry) od robota podczas teleoperacji
2. **Druga osoba** powinna obserwować robota i mieć dostęp do przycisku awaryjnego
3. **Powolne ruchy** na początku - przetestuj reakcje robota
4. **Stop awaryjny**: Naciśnij oba joysticki jednocześnie (w trybie kontrolera)
5. **Wyjście awaryjne**: Przycisk A na prawym kontrolerze (w trybie motion)

### Procedura bezpiecznego wyłączenia

```bash
# NIE ZAMYKAJ PROGRAMU GWAŁTOWNIE (Ctrl+C)
# Zamiast tego:
```

1. Powoli przesuń ramiona robota do pozycji początkowej
2. Naciśnij `q` w terminalu
3. Program automatycznie wykona bezpieczne zamknięcie (5 sekund)
4. Ramiona powrócą do pozycji spoczynkowej

### Monitorowanie stanu robota

Otwórz osobny terminal do monitorowania:
```bash
# Monitoruj temperatury motorów
watch -n 1 'unitree_sdk2_python przykład sprawdzania statusu'

# Monitoruj obciążenie CPU
htop
```

---

## 📚 Część 10: Dodatkowe zasoby

### Oficjalna dokumentacja
- [Unitree Teleoperation](https://support.unitree.com/home/zh/Teleoperation)
- [xr_teleoperate Wiki](https://github.com/unitreerobotics/xr_teleoperate/wiki)
- [XR Device Wiki](https://github.com/unitreerobotics/xr_teleoperate/wiki/XR_Device)

### Społeczność i wsparcie
- [Discord](https://discord.gg/ZwcVwxv5rq)
- [GitHub Issues](https://github.com/unitreerobotics/xr_teleoperate/issues)
- [DeepWiki Q&A](https://deepwiki.com/unitreerobotics/xr_teleoperate)

### Przydatne komendy do zapisania

Utwórz alias dla szybkiego uruchamiania:
```bash
echo 'alias quest3-teleop="cd ~/xr_teleoperate/teleop && python teleop_hand_and_arm.py --input-mode=controller --arm=G1_29 --ee=dex3"' >> ~/.bashrc
source ~/.bashrc
```

Teraz możesz uruchomić przez:
```bash
quest3-teleop
```

---

## ✅ Część 11: Checklist przed pierwszym uruchomieniem

Użyj tej listy, aby upewnić się, że wszystko jest skonfigurowane:

- [ ] Quest 3 jest naładowany (minimum 50%)
- [ ] Kontrolery mają świeże baterie
- [ ] Quest 3 i komputer są w tej samej sieci WiFi
- [ ] Znasz adres IP komputera sterującego
- [ ] Certyfikaty SSL zostały wygenerowane i zainstalowane
- [ ] Porty 8012 i 60001 są otwarte w firewall
- [ ] Zainstalowane środowisko conda 'tv'
- [ ] Zainstalowane `xr_teleoperate` i zależności
- [ ] Usługa obrazu działa na PC2 (dla fizycznego robota)
- [ ] Robot Unitree jest włączony i w trybie gotowości
- [ ] Obszar roboczy jest bezpieczny i wolny od przeszkód
- [ ] Druga osoba jest dostępna do monitorowania bezpieczeństwa
- [ ] Przeczytana dokumentacja bezpieczeństwa Unitree

---

## 🎯 Podsumowanie

Meta Quest 3 oferuje doskonałą platformę do teleoperacji robotów Unitree, łącząc przystępną cenę z wysoką jakością śledzenia. Kluczowe punkty:

1. **Tryb kontrolera** jest zalecany dla zadań wymagających precyzji
2. **Śledzenie dłoni** jest bardziej naturalne, ale wymaga dobrych warunków
3. **Sieć WiFi 5GHz** znacząco poprawia wydajność
4. **Bezpieczeństwo** jest najważniejsze - zawsze przestrzegaj procedur

Powodzenia w teleoperacji! 🤖🎮
