<div align="center">
  <h1 align="center">xr_teleoperate - Sterowanie robotem humanoidalnym przez urządzenia XR</h1>
  <a href="https://www.unitree.com/" target="_blank">
    <img src="https://www.unitree.com/images/0079f8938336436e955ea3a98c4e1e59.svg" alt="Unitree LOGO" width="15%">
  </a>
  <p align="center">
    <a href="README.md"> English </a> | <a href="README_zh-CN.md">中文</a> | <a href="README_ja-JP.md">日本語</a> | <a> Polski </a>
  </p>
  <p align="center">
    <a href="https://github.com/unitreerobotics/xr_teleoperate/wiki" target="_blank"> <img src="https://img.shields.io/badge/GitHub-Wiki-181717?logo=github" alt="Unitree LOGO"></a> <a href="https://discord.gg/ZwcVwxv5rq" target="_blank"><img src="https://img.shields.io/badge/-Discord-5865F2?style=flat&logo=Discord&logoColor=white" alt="Unitree LOGO"> <a href="https://deepwiki.com/unitreerobotics/xr_teleoperate"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a> </a>
  </p>
</div>


# 📺 Filmy demonstracyjne

<p align="center">
  <table>
    <tr>
      <td align="center" width="50%">
        <a href="https://www.youtube.com/watch?v=OTWHXTu09wE" target="_blank">
          <img src="https://img.youtube.com/vi/OTWHXTu09wE/maxresdefault.jpg" alt="Video 1" width="75%">
        </a>
        <p><b> G1 (29DoF) + Dex3-1 </b></p>
      </td>
      <td align="center" width="50%">
        <a href="https://www.youtube.com/watch?v=pNjr2f_XHoo" target="_blank">
          <img src="https://img.youtube.com/vi/pNjr2f_XHoo/maxresdefault.jpg" alt="Video 2" width="75%">
        </a>
        <p><b> H1_2 (Ramię 7DoF) </b></p>
      </td>
    </tr>
  </table>
</p>


# 🔖[Informacje o wydaniach](CHANGELOG_pl.md)

## 🏷️ v1.5 (2025.12.29)

- wsparcie dla trybu symulacji
- dodanie parametru nazwy interfejsu dla CycloneDDS
- [dodanie cache'owania aby przyspieszyć wczytywanie plików URDF](https://github.com/unitreerobotics/xr_teleoperate/commit/6cab654620735bfa347c1cd32a0d8c0c1e6ec343)
- ...



# 0. 📖 Wprowadzenie - Co to jest teleoperation?

## Czym jest teleoperation (zdalne sterowanie)?

To repozytorium implementuje system **teleoperation** (zdalnego sterowania) **robota humanoidalnego Unitree** przy użyciu **urządzeń XR (Extended Reality)** takich jak Apple Vision Pro, PICO 4 Ultra Enterprise lub Meta Quest 3. 

**Teleoperation** to metoda sterowania robotem, w której operator na żywo kontroluje ruchy robota za pomocą specjalnych urządzeń (w tym przypadku gogli VR/AR). Robot powtarza ruchy operatora w czasie rzeczywistym - gdy poruszasz ręką w googlach, robot również porusza swoim ramieniem!

## Dla kogo jest ten projekt?

Ten projekt jest przeznaczony dla:
- **Studentów** uczących się robotyki i chcących zrozumieć, jak sterować humanoidalnymi robotami
- **Początkujących programistów** zainteresowanych tematyką robotyki i rzeczywistości rozszerzonej
- **Badaczy** pracujących nad projektami związanymi z uczeniem maszynowym robotów (imitation learning)
- **Entuzjastów robotyki** pragnących poznać nowoczesne technologie sterowania

## Wymagania wstępne

> **WAŻNE dla początkujących**: Jeśli nigdy wcześniej nie pracowałeś z robotem Unitree, **koniecznie** przeczytaj co najmniej rozdział "Application Development" w [oficjalnej dokumentacji](https://support.unitree.com/main/en) przed rozpoczęciem pracy.
> 
> Dodatkowo, [Wiki tego repozytorium](https://github.com/unitreerobotics/xr_teleoperate/wiki) zawiera bogaty zbiór wiedzy podstawowej, do której możesz się odwoływać w dowolnym momencie.

## Diagram systemu - jak to działa?

Poniższy diagram pokazuje, jakie urządzenia są potrzebne i jak są one ze sobą połączone:

<p align="center">
  <a href="https://oss-global-cdn.unitree.com/static/55fb9cd245854810889855010da296f7_3415x2465.png">
    <img src="https://oss-global-cdn.unitree.com/static/55fb9cd245854810889855010da296f7_3415x2465.png" alt="System Diagram" style="width: 100%;">
  </a>
</p>

**Wyjaśnienie komponentów:**
1. **Urządzenie XR** (gogle VR/AR) - tutaj widzisz obraz z kamery robota i sterujesz jego ruchami
2. **Komputer Host** - komputer na którym uruchamiasz główny program sterujący
3. **Robot Unitree** (G1 lub H1) - robot humanoidalny, którym będziesz sterować
4. **Router WiFi** - zapewnia komunikację między wszystkimi urządzeniami


## Wspierane urządzenia

Aktualnie wspierane urządzenia w tym repozytorium:

<table>
  <tr>
    <th align="center">🤖 Robot</th>
    <th align="center">⚪ Status</th>
  </tr>
  <tr>
    <td align="center"><a href="https://www.unitree.com/cn/g1" target="_blank">G1 (29 DoF)</a></td>
    <td align="center">✅ Kompletne</td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.unitree.com/cn/g1" target="_blank">G1 (23 DoF)</a></td>
    <td align="center">✅ Kompletne</td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.unitree.com/cn/h1" target="_blank">H1 (ramię 4‑DoF)</a></td>
    <td align="center">✅ Kompletne</td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.unitree.com/cn/h1" target="_blank">H1_2 (ramię 7‑DoF)</a></td>
    <td align="center">✅ Kompletne</td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.unitree.com/cn/Dex1-1" target="_blank">Chwytaki Dex1‑1</a></td>
    <td align="center">✅ Kompletne</td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.unitree.com/cn/Dex3-1" target="_blank">Dłonie zręcznościowe Dex3‑1</a></td>
    <td align="center">✅ Kompletne</td>
  </tr>
  <tr>
    <td align="center"><a href="https://support.unitree.com/home/zh/G1_developer/inspire_dfx_dexterous_hand" target="_blank">Dłonie zręcznościowe Inspire</a></td>
    <td align="center">✅ Kompletne</td>
  </tr>
  <tr>
    <td style="text-align: center;"> <a href="https://www.brainco-hz.com/docs/revolimb-hand/" target="_blank"> Dłonie zręcznościowe BrainCo </td>
    <td style="text-align: center;"> &#9989; Kompletne </td>
  </tr>
  <tr>
    <td align="center"> ··· </td>
    <td align="center"> ··· </td>
  </tr>
</table>



# 1. 📦 Instalacja - Krok po kroku dla początkujących

## Co to jest środowisko wirtualne i dlaczego go używamy?

Zanim zaczniemy instalację, ważne jest zrozumienie koncepcji **środowiska wirtualnego**. Jest to izolowana przestrzeń dla Twojego projektu, która:
- Pozwala instalować specyficzne wersje bibliotek tylko dla tego projektu
- Zapobiega konfliktom między różnymi projektami
- Ułatwia zarządzanie zależnościami

Używamy narzędzia **conda** do zarządzania środowiskami wirtualnymi.

Ten projekt był testowany na Ubuntu 20.04 i Ubuntu 22.04. Inne systemy operacyjne mogą wymagać innych konfiguracji. Ten dokument opisuje przede wszystkim **tryb domyślny**.

Więcej informacji znajdziesz w [Oficjalnej Dokumentacji ](https://support.unitree.com/home/zh/Teleoperation) oraz [OpenTeleVision](https://github.com/OpenTeleVision/TeleVision).

## 1.1 📥 Instalacja podstawowa

### Krok 1: Utworzenie środowiska conda

Najpierw utworzymy izolowane środowisko Python z potrzebnymi bibliotekami:

```bash
# Utwórz nowe środowisko conda o nazwie 'tv' z Pythonem 3.10
# pinocchio=3.1.0 - biblioteka do kinematyki robota
# numpy=1.26.4 - biblioteka do obliczeń numerycznych
# -c conda-forge - instaluje z repozytorium conda-forge
(base) unitree@Host:~$ conda create -n tv python=3.10 pinocchio=3.1.0 numpy=1.26.4 -c conda-forge

# Aktywuj nowo utworzone środowisko
# Od teraz wszystkie komendy będą wykonywane w tym środowisku
(base) unitree@Host:~$ conda activate tv
```

**Wyjaśnienie promptu:**
- `(base)` lub `(tv)` - nazwa aktywnego środowiska conda
- `unitree@Host` - nazwa użytkownika @ nazwa komputera
- `~` - aktualny katalog (~ oznacza katalog domowy)
- `$` - oznacza shell Bash dla zwykłego użytkownika

### Krok 2: Pobranie repozytorium

```bash
# Sklonuj (pobierz) repozytorium z GitHuba do swojego komputera
(tv) unitree@Host:~$ git clone https://github.com/unitreerobotics/xr_teleoperate.git

# Przejdź do katalogu projektu
(tv) unitree@Host:~$ cd xr_teleoperate

# Pobierz submoduły (dodatkowe zależności projektu)
# --init - inicjalizuje submoduły
# --depth 1 - pobiera tylko najnowszą wersję (oszczędza czas i miejsce)
(tv) unitree@Host:~/xr_teleoperate$ git submodule update --init --depth 1
```

### Krok 3: Instalacja modułu teleimager

**Co to jest teleimager?** To biblioteka obsługująca strumienie obrazu z kamer robota.

```bash
# Przejdź do katalogu teleimager
(tv) unitree@Host:~/xr_teleoperate$ cd teleop/teleimager

# Zainstaluj moduł w trybie edycji (-e)
# Tryb edycji pozwala na modyfikację kodu bez ponownej instalacji
# --no-deps - nie instaluje zależności (już je mamy)
(tv) unitree@Host:~/xr_teleoperate/teleop/teleimager$ pip install -e . --no-deps
```

### Krok 4: Instalacja modułu televuer

**Co to jest televuer?** To biblioteka obsługująca komunikację z urządzeniami XR (gogle VR/AR).

```bash
# Przejdź do katalogu televuer
(tv) unitree@Host:~/xr_teleoperate$ cd teleop/televuer

# Zainstaluj moduł wraz z zależnościami
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ pip install -e .
```

### Krok 5: Konfiguracja certyfikatów SSL (ważne dla bezpieczeństwa!)

**Dlaczego potrzebujemy certyfikatów?** Certyfikaty SSL zapewniają bezpieczne, szyfrowane połączenie między Twoim komputerem a urządzeniem XR. To standardowy protokół bezpieczeństwa używany w internecie.

#### Dla urządzeń Pico / Quest (prostszy proces):

```bash
# Wygeneruj pliki certyfikatów (ważne przez 365 dni)
# -x509 - tworzy certyfikat samopodpisany
# -nodes - nie szyfruj klucza prywatnego hasłem
# -days 365 - certyfikat ważny przez rok
# -newkey rsa:2048 - utwórz nowy klucz RSA 2048-bitowy
# -keyout key.pem - zapisz klucz prywatny do key.pem
# -out cert.pem - zapisz certyfikat do cert.pem
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out cert.pem
```

#### Dla Apple Vision Pro (wymaga dodatkowych kroków):

Apple Vision Pro wymaga bardziej zaawansowanej konfiguracji certyfikatów:

```bash
# Krok 1: Wygeneruj klucz główny CA (Certificate Authority)
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ openssl genrsa -out rootCA.key 2048

# Krok 2: Utwórz certyfikat główny CA
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 365 -out rootCA.pem -subj "/CN=xr-teleoperate"

# Krok 3: Wygeneruj klucz serwera
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ openssl genrsa -out key.pem 2048

# Krok 4: Utwórz żądanie podpisania certyfikatu (CSR)
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ openssl req -new -key key.pem -out server.csr -subj "/CN=localhost"

# Krok 5: Utwórz plik konfiguracyjny z alternatywnymi nazwami
# WAŻNE: Zamień IP.2 na adres IP swojego komputera!
# Sprawdź swój adres IP komendą: ifconfig
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ vim server_ext.cnf
# Wpisz następującą zawartość:
subjectAltName = @alt_names
[alt_names]
DNS.1 = localhost
IP.1 = 192.168.123.164
IP.2 = 192.168.123.2  # <-- ZAMIEŃ NA SWÓJ ADRES IP!

# Krok 6: Podpisz certyfikat serwera
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ openssl x509 -req -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out cert.pem -days 365 -sha256 -extfile server_ext.cnf

# Krok 7: Sprawdź czy wszystkie pliki zostały utworzone
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ ls
# Powinieneś zobaczyć: cert.pem, key.pem, rootCA.key, rootCA.pem, etc.

# Krok 8: Prześlij rootCA.pem do Apple Vision Pro przez AirDrop i zainstaluj go
# To pozwoli Vision Pro zaufać Twojemu certyfikatowi
```

#### Konfiguracja firewalla (aby umożliwić połączenia):

```bash
# Otwórz port 8012 w firewallu
# Port 8012 jest używany przez serwer televuer
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ sudo ufw allow 8012
```

#### Wybierz jedną z metod konfiguracji ścieżek certyfikatów:

**Metoda 1: Katalog konfiguracyjny użytkownika (zalecane):**

```bash
# Utwórz katalog konfiguracyjny
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ mkdir -p ~/.config/xr_teleoperate/

# Skopiuj certyfikaty do katalogu konfiguracyjnego
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ cp cert.pem key.pem ~/.config/xr_teleoperate/
```

**Metoda 2: Zmienne środowiskowe:**

```bash
# Dodaj ścieżki certyfikatów do zmiennych środowiskowych
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ echo 'export XR_TELEOP_CERT="$HOME/xr_teleoperate/teleop/televuer/cert.pem"' >> ~/.bashrc
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ echo 'export XR_TELEOP_KEY="$HOME/xr_teleoperate/teleop/televuer/key.pem"' >> ~/.bashrc

# Przeładuj konfigurację bash
(tv) unitree@Host:~/xr_teleoperate/teleop/televuer$ source ~/.bashrc
```


## 1.2 🕹️ Instalacja unitree_sdk2_python

**Co to jest unitree_sdk2_python?** To oficjalna biblioteka Python od Unitree, która umożliwia komunikację z robotem. Bez niej nie będziesz mógł wysyłać komend do robota!

```bash
# Wróć do katalogu domowego
(tv) unitree@Host:~$ cd ~

# Sklonuj repozytorium SDK
(tv) unitree@Host:~$ git clone https://github.com/unitreerobotics/unitree_sdk2_python.git

# Przejdź do katalogu SDK
(tv) unitree@Host:~$ cd unitree_sdk2_python

# Zainstaluj SDK w trybie edycji
(tv) unitree@Host:~/unitree_sdk2_python$ pip install -e .
```

> **Ważne uwagi:**
> 
> **Uwaga 1:** Dla `xr_teleoperate` w wersji **v1.1 i nowszych**, upewnij się, że repozytorium `unitree_sdk2_python` jest w wersji **równej lub nowszej niż** [404fe44d76f705c002c97e773276f2a8fefb57e4](https://github.com/unitreerobotics/unitree_sdk2_python/commit/404fe44d76f705c002c97e773276f2a8fefb57e4).
>
> **Uwaga 2**: Biblioteka [unitree_dds_wrapper](https://github.com/unitreerobotics/unitree_dds_wrapper) z oryginalnej gałęzi h1_2 była wersją tymczasową. Została teraz w pełni przeniesiona do oficjalnej biblioteki komunikacji opartej na Pythonie: [unitree_sdk2_python](https://github.com/unitreerobotics/unitree_sdk2_python).
>
> **Uwaga 3**: Wszystkie identyfikatory przed komendą służą do podpowiedzi: **Na jakim urządzeniu i w jakim katalogu powinna być wykonana komenda**.
>
> W pliku `~/.bashrc` systemu Ubuntu domyślna konfiguracja to: `PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '`
>
> Przykład komendy `(tv) unitree@Host:~$ pip install meshcat`:
>
> - `(tv)` Wskazuje, że shell znajduje się w środowisku conda o nazwie `tv`.
> - `unitree@Host:~` Pokazuje, że użytkownik `\u` `unitree` jest zalogowany na urządzeniu `\h` `Host`, z bieżącym katalogiem roboczym `\w` jako `$HOME` (~).
> - `$` pokazuje, że obecny shell to Bash (dla użytkowników niebędących rootem).
> - `pip install meshcat` to komenda, którą `unitree` chce wykonać na `Host`.
>
> Możesz zapoznać się z [Przewodnikiem Harleya Hahna po Unix i Linux](https://www.harley.com/unix-book/book/chapters/04.html#H) oraz [Przewodnikiem użytkownika Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html), aby dowiedzieć się więcej.



## 1.3 🚀 Opis parametrów uruchomienia

### Podstawowe parametry sterowania

Oto najważniejsze parametry, których będziesz używać:

|      ⚙️ Parametr      |                        📜 Opis                         |                     🔘 Dostępne opcje                      |     📌 Domyślna wartość     |
| :-------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :---------------: |
|     `--frequency`     |            Ustaw częstotliwość (FPS) nagrywania i sterowania. Określa jak często robot aktualizuje swoją pozycję.             |                  Dowolna rozsądna wartość zmiennoprzecinkowa                  |       30.0        |
|    `--input-mode`     |       Wybierz tryb wejścia XR (jak sterujesz robotem). **hand** = śledź ruchy dłoni, **controller** = użyj kontrolerów VR        |   `hand` (śledzenie dłoni)<br>`controller` (śledzenie kontrolera)   |      `hand`       |
|   `--display-mode`    |  Wybierz tryb wyświetlania XR (jak widzisz perspektywę robota)  | `immersive` (immersyjny - tylko widok z robota)<br>`ego` (pass-through + małe okno pierwszej osoby)<br>`pass-through` (tylko pass-through) |    `immersive`    |
|        `--arm`        |      Wybierz typ ramienia robota (patrz rozdział 0. 📖 Wprowadzenie)       |                 `G1_29` `G1_23` `H1_2` `H1`                  |      `G1_29`      |
|        `--ee`         | Wybierz typ efektora końcowego (end-effector) ramienia - tj. chwytaka lub dłoni zręcznościowej (patrz 0. 📖 Wprowadzenie) |     `dex1` `dex3` `inspire_ftp` `inspire_dfx` `brainco`      |       None        |
|   `--img-server-ip`   | Ustaw adres IP serwera obrazu do odbierania strumieni wideo i konfiguracji sygnalizacji WebRTC. To adres komputera obliczeniowego robota (PC2). |                        Adres `IPv4`                        | `192.168.123.164` |
| `--network-interface` |    Ustaw interfejs sieciowy dla komunikacji CycloneDDS. Użyj nazwy interfejsu jak eth0, wlan0. Zwykle można pominąć.    |                    Nazwa interfejsu sieciowego                    |      `None`       |

### Parametry przełączania trybu

Te parametry włączają zaawansowane funkcje:

| ⚙️ Parametr  |                        📜 Opis                         |
| :----------: | :----------------------------------------------------------: |
|  `--motion`  | **Włącz tryb sterowania ruchem.** Gdy włączony, program teleoperation może działać równolegle z programem sterowania ruchem robota. W trybie **śledzenia dłoni** można użyć [pilota R3](https://www.unitree.com/cn/R3) do kontrolowania normalnego chodu robota; w trybie **śledzenia kontrolera** joysticki również mogą kontrolować ruch robota. |
| `--headless` | **Włącz tryb bezgłowy (headless).** Do uruchamiania programu na urządzeniach bez wyświetlacza, np. na jednostce obliczeniowej robota (PC2). |
|   `--sim`    | **Włącz [tryb symulacji](https://github.com/unitreerobotics/unitree_sim_isaaclab).** Pozwala testować program bez fizycznego robota! |
|   `--ipc`    | **Tryb komunikacji międzyprocesowej.** Umożliwia kontrolowanie stanu programu xr_teleoperate przez IPC. Odpowiedni do interakcji z programami agentów. |
| `--affinity` | **Tryb powinowactwa CPU.** Ustawia przypisanie rdzeni CPU. Jeśli nie wiesz co to jest, nie ustawiaj tego parametru. |
|  `--record`  | **Włącz tryb nagrywania danych.** Naciśnij **r** aby rozpocząć teleoperation, następnie **s** aby rozpocząć nagrywanie; naciśnij **s** ponownie aby zatrzymać i zapisać epizod. Powtarzaj proces naciskając **s**. Przydatne do zbierania danych treningowych dla uczenia maszynowego! |
|  `--task-*`  | Skonfiguruj ścieżkę zapisu, cel, opis i kroki nagrywanego zadania. Używane z `--record`. |

## 1.4 🔄 Diagram przejść stanów

Ten diagram pokazuje jak program przechodzi między różnymi stanami podczas pracy:

<p align="center">
  <a href="https://oss-global-cdn.unitree.com/static/712c312b0ac3401f8d7d9001b1e14645_11655x4305.jpg">
    <img src="https://oss-global-cdn.unitree.com/static/712c312b0ac3401f8d7d9001b1e14645_11655x4305.jpg" alt="System Diagram" style="width: 85%;">
  </a>
</p>

**Wyjaśnienie stanów:**
- **Ready (Gotowy)** - Program czeka na rozpoczęcie teleoperation
- **Running (Działa)** - Robot aktywnie śledzi Twoje ruchy
- **Recording (Nagrywanie)** - Robot śledzi ruchy I nagrywa dane
- **Saving (Zapisywanie)** - Dane są zapisywane na dysk

# 2. 💻 Wdrożenie w symulacji - Bezpieczne testowanie bez robota!

## Co to jest symulacja i dlaczego jest przydatna?

**Symulacja** to wirtualne środowisko, które naśladuje zachowanie prawdziwego robota. Używamy symulatora [Isaac Lab](https://github.com/unitreerobotics/unitree_sim_isaaclab) od NVIDIA.

**Zalety symulacji:**
- ✅ Bezpieczne - nie ma ryzyka uszkodzenia sprzętu
- ✅ Wygodne - można testować bez dostępu do fizycznego robota
- ✅ Szybsze uczenie - łatwe resetowanie i powtarzanie scenariuszy
- ✅ Ekonomiczne - nie zużywa energii ani części robota

## 2.1 📥 Konfiguracja środowiska symulacyjnego

### Krok 1: Instalacja Isaac Lab

Najpierw zainstaluj symulator [unitree_sim_isaaclab](https://github.com/unitreerobotics/unitree_sim_isaaclab). Postępuj zgodnie z README tego repozytorium.

### Krok 2: Uruchomienie symulacji

Uruchom symulację z konfiguracją robota G1 (29 DoF) i dłonią zręcznościową Dex3:

```bash
# Aktywuj środowisko symulacji
(base) unitree@Host:~$ conda activate unitree_sim_env

# Przejdź do katalogu symulatora
(unitree_sim_env) unitree@Host:~$ cd ~/unitree_sim_isaaclab

# Uruchom symulację z odpowiednimi parametrami
# --device cpu - użyj CPU (możesz użyć 'gpu' jeśli masz kartę NVIDIA)
# --enable_cameras - włącz kamery w symulacji
# --task Isaac-PickPlace-Cylinder-G129-Dex3-Joint - wybierz zadanie podnoszenia cylindra
# --enable_dex3_dds - włącz komunikację DDS dla dłoni Dex3
# --robot_type g129 - typ robota G1 z 29 stopniami swobody
(unitree_sim_env) unitree@Host:~/unitree_sim_isaaclab$ python sim_main.py --device cpu --enable_cameras --task Isaac-PickPlace-Cylinder-G129-Dex3-Joint --enable_dex3_dds --robot_type g129
```

💥💥💥 UWAGA❗

> **Po uruchomieniu symulacji, kliknij raz w oknie, aby je aktywować.**
>
> Terminal pokaże:  `controller started, start main loop...`

Oto jak wygląda interfejs symulacji:

<p align="center">   <a href="https://oss-global-cdn.unitree.com/static/bea51ef618d748368bf59c60f4969a65_1749x1090.png">     <img src="https://oss-global-cdn.unitree.com/static/bea51ef618d748368bf59c60f4969a65_1749x1090.png" alt="Simulation UI" style="width: 75%;">   </a> </p>

## 2.2 🚀 Uruchomienie programu sterowania

Ten program obsługuje sterowanie XR zarówno fizycznym robotem jak i w symulacji. Wybierz tryby za pomocą argumentów wiersza poleceń.

### Przykład: Śledzenie dłoni z G1(29 DoF) + Dex3 w symulacji z nagrywaniem

**Pełna komenda z wszystkimi parametrami:**

```bash
# Przejdź do katalogu teleop
(tv) unitree@Host:~$ cd ~/xr_teleoperate/teleop/

# Uruchom program z pełnymi parametrami
(tv) unitree@Host:~/xr_teleoperate/teleop/$ python teleop_hand_and_arm.py --input-mode=hand --arm=G1_29 --ee=dex3 --sim --record
```

**Uproszczona komenda (wartości domyślne):**

```bash
# Wiele parametrów ma wartości domyślne, więc możemy je pominąć
(tv) unitree@Host:~/xr_teleoperate/teleop/$ python teleop_hand_and_arm.py --ee=dex3 --sim --record
```

**Co oznaczają te parametry:**
- `--ee=dex3` - używamy dłoni zręcznościowej Dex3
- `--sim` - tryb symulacji (bez tego program próbowałby połączyć się z fizycznym robotem)
- `--record` - włącz możliwość nagrywania danych

### Co powinno się pojawić po uruchomieniu

Po uruchomieniu programu, terminal wyświetli informacje o inicjalizacji:

<p align="center">   <a href="https://oss-global-cdn.unitree.com/static/735464d237214f6c9edf8c7db9847a0a_1874x1275.png">     <img src="https://oss-global-cdn.unitree.com/static/735464d237214f6c9edf8c7db9847a0a_1874x1275.png" alt="Terminal Start Log" style="width: 75%;">   </a> </p>

### Kolejne kroki - Połączenie z urządzeniem XR:

#### Krok 1: Załóż gogle XR
Załóż swój headset XR (np. Apple Vision Pro, PICO 4, Meta Quest 3, etc.)

#### Krok 2: Połącz się z siecią Wi-Fi
Upewnij się, że gogle są podłączone do tej samej sieci Wi-Fi co Twój komputer.

#### Krok 3: (Opcjonalny) Test WebRTC dla kamery głowy

> **Ten krok jest potrzebny tylko jeśli:**
> - Twoja kamera głowy ma włączoną funkcję WebRTC (`cam_config_server.yaml → head_camera → enable_webrtc: true`)
> - **Jeśli NIE**, pomiń do Kroku 4.

Otwórz przeglądarkę w googlach (np. Safari lub PICO Browser) i przejdź do:  
**https://192.168.123.164:60001**

> **Uwaga 1:** Ten adres IP to adres **PC2** - komputera obliczeniowego robota (lub komputera z symulacją) uruchamiającego usługę teleimager.  
> 
> **Uwaga 2:** Zobaczysz ostrzeżenie o bezpieczeństwie (podobnie jak w kroku 4 poniżej). Kliknij **Zaawansowane (Advanced)**, następnie **Kontynuuj do IP (niebezpieczne) (Proceed to IP (unsafe))**. Po załadowaniu strony, naciśnij przycisk **start** w lewym górnym rogu; jeśli zobaczysz podgląd z kamery głowy, test się powiódł.
>
> <p align="center">
>   <a href="https://oss-global-cdn.unitree.com/static/777f9c6f42d74eb2a6438d1509a73025_2475x1574.jpg">
>     <img src="https://oss-global-cdn.unitree.com/static/777f9c6f42d74eb2a6438d1509a73025_2475x1574.jpg" alt="webrtc_unsafe" style="width: 50%;">
>   </a>
> </p>
>
> **Uwaga 3:** Ten krok ma dwa cele:  
>
> 1. Weryfikację, że usługa teleimager działa poprawnie.  
> 2. Ręczne zaufanie samopodpisanemu certyfikatowi WebRTC.  
>
> Po wykonaniu tego raz na tym samym urządzeniu z tym samym certyfikatem, możesz pominąć ten krok przy kolejnych uruchomieniach.

#### Krok 4: Połączenie z interfejsem Vuer

Otwórz przeglądarkę (np. Safari lub PICO Browser) i przejdź do:  
`https://192.168.123.2:8012/?ws=wss://192.168.123.2:8012`

> **Uwaga 1**: Ten adres IP musi odpowiadać adresowi IP Twojego **komputera Host** (sprawdź komendą `ifconfig`).
>
> **Uwaga 2**: Zobaczysz ostrzeżenie o bezpieczeństwie. Kliknij **Zaawansowane (Advanced)**, następnie **Kontynuuj do IP (niebezpieczne) (Proceed to IP (unsafe))**.

<p align="center">
  <a href="https://oss-global-cdn.unitree.com/static/cef18751ca6643b683bfbea35fed8e7c_1279x1002.png">
    <img src="https://oss-global-cdn.unitree.com/static/cef18751ca6643b683bfbea35fed8e7c_1279x1002.png" alt="vuer_unsafe" style="width: 50%;">
  </a>
</p>

#### Krok 5: Uruchom sesję VR

Na stronie Vuer, kliknij przycisk **Virtual Reality**. Zaakceptuj wszystkie prośby o uprawnienia, aby rozpocząć sesję VR.

<p align="center">  <a href="https://oss-global-cdn.unitree.com/static/fdeee4e5197f416290d8fa9ecc0b28e6_2480x1286.png">    <img src="https://oss-global-cdn.unitree.com/static/fdeee4e5197f416290d8fa9ecc0b28e6_2480x1286.png" alt="Vuer UI" style="width: 75%;">  </a> </p>

#### Krok 6: Sprawdzenie połączenia

W googlach zobaczysz widok z perspektywy pierwszej osoby robota. Terminal wyświetli informacje o połączeniu:

```bash
websocket is connected. id:dbb8537d-a58c-4c57-b49d-cbb91bd25b90
default socket worker is up, adding clientEvents
Uplink task running. id:dbb8537d-a58c-4c57-b49d-cbb91bd25b90
```

**Co to oznacza:**
- `websocket is connected` - połączenie WebSocket między googlami a komputerem zostało nawiązane
- `id:dbb8537d...` - unikalny identyfikator sesji
- `Uplink task running` - zadanie komunikacji działa prawidłowo

#### Krok 7: Wyrównaj pozę

**WAŻNE:** Wyrównaj swoje ramiona do **początkowej pozy robota**, aby uniknąć nagłych ruchów przy starcie!

<p align="center">  <a href="https://oss-global-cdn.unitree.com/static/2522a83214744e7c8c425cc2679a84ec_670x867.png">    <img src="https://oss-global-cdn.unitree.com/static/2522a83214744e7c8c425cc2679a84ec_670x867.png" alt="Initial Pose" style="width: 25%;">  </a> </p>

**Dlaczego to ważne:**
Jeśli Twoje ramiona będą w innej pozycji niż robot w momencie uruchomienia sterowania, robot spróbuje szybko przenieść się do Twojej pozycji, co może być niebezpieczne lub uszkodzić sprzęt!

#### Krok 8: Rozpocznij teleoperation

W terminalu naciśnij klawisz **r** (od "run"), aby rozpocząć teleoperation. Teraz możesz sterować ramieniem robota i dłonią zręcznościową!

**Sterowanie:**
- Poruszaj swoimi ramionami → robot porusza ramionami
- Poruszaj dłońmi → robot porusza palcami dłoni zręcznościowej

#### Krok 9: Nagrywanie danych (opcjonalne)

Podczas teleoperation:
- Naciśnij **s** (od "save"), aby **rozpocząć nagrywanie**
- Wykonaj zadanie (np. podnieś obiekt)
- Naciśnij **s** ponownie, aby **zatrzymać i zapisać** nagranie

Możesz powtarzać ten proces wielokrotnie, aby zebrać wiele przykładów tego samego zadania.

<p align="center">  <a href="https://oss-global-cdn.unitree.com/static/f5b9b03df89e45ed8601b9a91adab37a_2397x1107.png">    <img src="https://oss-global-cdn.unitree.com/static/f5b9b03df89e45ed8601b9a91adab37a_2397x1107.png" alt="Recording Process" style="width: 75%;">  </a> </p>

> **Uwaga 1**: Nagrane dane są domyślnie przechowywane w `xr_teleoperate/teleop/utils/data`, z instrukcjami użycia w tym repozytorium:  [unitree_IL_lerobot](https://github.com/unitreerobotics/unitree_IL_lerobot/tree/main?tab=readme-ov-file#data-collection-and-conversion).
>
> **Uwaga 2**: Zwróć uwagę na rozmiar przestrzeni dyskowej podczas nagrywania danych. Nagrania wideo zajmują dużo miejsca!
>
> **Uwaga 3**: W wersji v1.4 i nowszych, okno "record image" zostało usunięte.

## 2.3 🔚 Zamykanie programu

Aby bezpiecznie zakończyć program, naciśnij klawisz **q** (od "quit") w terminalu.

**Co się dzieje po naciśnięciu 'q':**
- Program zatrzymuje sterowanie robotem
- Zapisuje ostatnie dane (jeśli nagrywanie było aktywne)
- Zamyka połączenie z urządzeniem XR
- Kończy działanie

# 3. 🤖 Wdrożenie na fizycznym robocie - Praca z prawdziwym sprzętem

## Różnice między symulacją a fizycznym robotem

Wdrożenie na fizycznym robocie jest podobne do symulacji, ale ma kilka kluczowych różnic:

1. **Bezpieczeństwo** - musisz zachować szczególną ostrożność!
2. **Usługa obrazu** - musisz ręcznie uruchomić serwis kamer
3. **Sprzęt dodatkowy** - mogą być potrzebne dodatkowe usługi dla dłoni zręcznościowych

## 3.1 🖼️ Konfiguracja usługi obrazu

**Dlaczego jest to potrzebne:**
W środowisku symulacyjnym, usługa obrazu jest automatycznie włączona. Dla fizycznego wdrożenia, musisz ręcznie uruchomić usługę obrazu na podstawie Twojego sprzętu kamerowego.

### Krok 1: Instalacja usługi obrazu na PC2 robota

**Co to jest PC2:**
PC2 to jednostka obliczeniowa wbudowana w robota Unitree (G1/H1/H1_2). To na niej uruchamiamy usługę zbierającą obraz z kamer.

```bash
# Połącz się przez SSH z PC2
# SSH (Secure Shell) - protokół umożliwiający zdalny dostęp do terminala innego komputera

# Przejdź do katalogu domowego
(base) unitree@PC2:~$ cd ~

# Sklonuj repozytorium usługi obrazu
(base) unitree@PC2:~$ git clone https://github.com/silencht/teleimager

# Skonfiguruj środowisko według instrukcji w README repozytorium teleimager
# Link: https://github.com/silencht/teleimager/blob/main/README.md
```

### Krok 2: Kopiowanie certyfikatów SSL

**Na Twoim lokalnym komputerze Host:**

```bash
# Skopiuj pliki certyfikatów z katalogu televuer do PC2
# scp - Secure Copy, narzędzie do bezpiecznego kopiowania plików przez sieć
# Składnia: scp <źródło> <użytkownik>@<adres_IP>:<katalog_docelowy>
(tv) unitree@Host:~$ scp ~/xr_teleoperate/teleop/televuer/key.pem ~/xr_teleoperate/teleop/televuer/cert.pem unitree@192.168.123.164:~/teleimager
```

**Na PC2 robota:**

```bash
# Przejdź do katalogu teleimager
(teleimager) unitree@PC2:~$ cd teleimager

# Utwórz katalog konfiguracyjny
(teleimager) unitree@PC2:~$ mkdir -p ~/.config/xr_teleoperate/

# Skopiuj certyfikaty do katalogu konfiguracyjnego
(teleimager) unitree@PC2:~/teleimager$ cp cert.pem key.pem ~/.config/xr_teleoperate/
```

### Krok 3: Uruchomienie usługi obrazu

**Na PC2 robota:**

```bash
# Skonfiguruj cam_config_server.yaml według dokumentacji teleimager
# Ten plik określa które kamery używać i jak je skonfigurować

# Uruchom serwer obrazu - pierwsza metoda
(teleimager) unitree@PC2:~/teleimager$ python -m teleimager.image_server

# LUB druga metoda (równoważna)
(teleimager) unitree@PC2:~/teleimager$ teleimager-server
```

**Co robi ta usługa:**
- Zbiera obrazy z kamer robota (głowa, nadgarstki)
- Kompresuje je dla efektywnej transmisji
- Wysyła je przez sieć do Twojego komputera Host

### Krok 4: Subskrypcja obrazów na komputerze Host

**Na Twoim lokalnym komputerze:**

```bash
# Przejdź do katalogu źródłowego teleimager
(tv) unitree@Host:~$ cd ~/xr_teleoperate/teleop/teleimager/src

# Uruchom klienta obrazu, który będzie odbierał strumienie z PC2
# --host 192.168.123.164 - adres IP PC2 robota
(tv) unitree@Host:~/xr_teleoperate/teleop/teleimager/src$ python -m teleimager.image_client --host 192.168.123.164
```

**Test WebRTC (opcjonalny):**
Jeśli skonfigurowałeś strumień obrazu WebRTC, możesz otworzyć URL [https://192.168.123.164:60001](https://192.168.123.164:60001) w przeglądarce i kliknąć przycisk Start, aby przetestować.

## 3.2 ✋ Usługa dłoni zręcznościowej Inspire (opcjonalnie)

> **Uwaga 1**: Pomiń ten krok, jeśli Twoja konfiguracja nie używa dłoni Inspire.
>
> **Uwaga 2**: Dla robota G1 z [dłonią Inspire DFX](https://support.unitree.com/home/zh/G1_developer/inspire_dfx_dexterous_hand), zobacz powiązany problem [#46](https://github.com/unitreerobotics/xr_teleoperate/issues/46).
>
> **Uwaga 3**: Dla [dłoni Inspire FTP](https://support.unitree.com/home/zh/G1_developer/inspire_ftp_dexterity_hand), zobacz powiązany problem [#48](https://github.com/unitreerobotics/xr_teleoperate/issues/48). Dłoń zręcznościowa FTP jest teraz obsługiwana. Sprawdź parametr `--ee` dla konfiguracji.

### Czym jest dłoń Inspire?

Dłoń Inspire to zaawansowana dłoń zręcznościowa firm trzeciej, która może być zamontowana na robotach Unitree. Wymaga osobnej usługi sterującej.

### Instalacja i konfiguracja:

```bash
# Na PC2 robota, zainstaluj zależności
unitree@PC2:~$ sudo apt install libboost-all-dev libspdlog-dev

# Sklonuj repozytorium (wykonaj to na swoim komputerze, potem skopiuj do PC2)
# Użyj tego URL: https://github.com/unitreerobotics/DFX_inspire_service

# Zbuduj projekt
unitree@PC2:~$ cd DFX_inspire_service && mkdir build && cd build
unitree@PC2:~/DFX_inspire_service/build$ cmake ..
unitree@PC2:~/DFX_inspire_service/build$ make -j6
```

### Uruchomienie usługi:

**Terminal 1 - Uruchom usługę sterowania dłońmi:**

```bash
# Dla robota Unitree G1:
unitree@PC2:~/DFX_inspire_service/build$ sudo ./inspire_g1

# LUB dla robota Unitree H1:
unitree@PC2:~/DFX_inspire_service/build$ sudo ./inspire_h1 -s /dev/ttyUSB0
```

**Terminal 2 - Test działania:**

```bash
# Uruchom przykładowy program testowy
unitree@PC2:~/DFX_inspire_service/build$ ./hand_example
```

**Co powinno się stać:**
Jeśli obie dłonie otwierają się i zamykają cyklicznie, oznacza to sukces! Po udanym teście, zamknij program `./hand_example` w Terminalu 2.

## 3.3 ✋ Usługa dłoni BrainCo (opcjonalnie)

Dla dłoni BrainCo, zapoznaj się z [README repozytorium](https://github.com/unitreerobotics/brainco_hand_service) w celu uzyskania instrukcji konfiguracji.

## 3.4 ✋ Usługa Unitree Dex1_1 (opcjonalnie)

Dla chwytaka Dex1_1, zapoznaj się z [README repozytorium](https://github.com/unitreerobotics/dex1_1_service) w celu uzyskania instrukcji konfiguracji.

## 3.5 🚀 Uruchomienie sterowania fizycznym robotem

>  ![Ostrzeżenie](https://img.shields.io/badge/Ostrzeżenie-Ważne-red)
>
>  **ZASADY BEZPIECZEŃSTWA - PRZECZYTAJ PRZED URUCHOMIENIEM!**
>
>  1. **Wszyscy muszą zachować bezpieczną odległość od robota**, aby zapobiec wszelkim potencjalnym niebezpieczeństwom! Robot jest silny i może poruszać się szybko.
>  2. **Przeczytaj [Oficjalną Dokumentację](https://support.unitree.com/home/zh/Teleoperation) co najmniej raz** przed uruchomieniem tego programu.
>  3. Aby użyć trybu ruchu (z `--motion`), upewnij się, że robot jest w trybie sterowania (przez [pilota R3](https://www.unitree.com/R3)).
>  4. **Miej zawsze przygotowany fizyczny przycisk awaryjnego zatrzymania!**
>  5. W trybie ruchu:
>    - Prawy kontroler przycisk **A** = Wyjście z teleoperation
>    - Oba joysticki wciśnięte jednocześnie = miękkie awaryjne zatrzymanie (przełączenie w tryb tłumienia)
>    - Lewy joystick = kierunki ruchu
>    - Prawy joystick = obracanie
>    - Maksymalna prędkość jest ograniczona w kodzie

**Uruchomienie programu:**

Proces jest taki sam jak w symulacji, ale **KONIECZNIE przestrzegaj powyższych ostrzeżeń bezpieczeństwa!**

```bash
# Przykład dla robota G1 z dłonią Dex3
(tv) unitree@Host:~/xr_teleoperate/teleop/$ python teleop_hand_and_arm.py --ee=dex3 --record

# Uwaga: Pomiń parametr --sim, aby program połączył się z fizycznym robotem!
```

## 3.6 🔚 Bezpieczne zamykanie programu

> ![Ostrzeżenie](https://img.shields.io/badge/Ostrzeżenie-Ważne-red)
>
> **Aby uniknąć uszkodzenia robota, zaleca się ustawienie ramion robota blisko pozy początkowej przed naciśnięciem **q** w celu wyjścia.**
>
> **Co się dzieje podczas zamykania:**
>
> - W **Trybie Debug**: Po naciśnięciu klawisza wyjścia, oba ramiona powrócą do **pozy początkowej** robota w ciągu 5 sekund, a następnie sterowanie się zakończy.
>
> - W **Trybie Motion**: Po naciśnięciu klawisza wyjścia, oba ramiona powrócą do **pozy sterowania ruchem** w ciągu 5 sekund, a następnie sterowanie się zakończy.

**Dlaczego to ważne:**
Nagłe zatrzymanie programu, gdy ramiona są daleko od pozycji początkowej, może spowodować szybkie ruchy podczas procedury zamykania, co może uszkodzić robot lub otoczenie!



# 4. 🗺️ Przegląd struktury kodu - Zrozumienie projektu

## Dla czego ta sekcja jest ważna?

Zrozumienie struktury projektu pomoże Ci:
- Wiedzieć gdzie szukać, gdy chcesz coś zmienić
- Rozumieć jak różne części systemu współpracują
- Łatwiej debugować problemy

## Struktura katalogów

```
xr_teleoperate/
│
├── assets/                    [Przechowuje pliki związane z URDF robota]
│                              URDF = Unified Robot Description Format
│                              To format XML opisujący kinematykę robota
│
├── teleop/
│   ├── teleimager/            [Nowa biblioteka usługi obrazu, obsługująca wiele funkcji]
│   │                          Odpowiada za zbieranie i przesyłanie obrazu z kamer
│   │
│   ├── televuer/
│   │      ├── src/televuer/
│   │         ├── television.py       [Przechwytuje dane głowy, nadgarstków i dłoni/kontrolera z urządzeń XR przy użyciu Vuer]
│   │         ├── tv_wrapper.py       [Przetwarzanie przechwyconych danych]
│   │      ├── test/
│   │         ├── _test_television.py [Program testowy dla television.py]
│   │         ├── _test_tv_wrapper.py [Program testowy dla tv_wrapper.py]
│   │
│   ├── robot_control/
│   │      ├── src/dex-retargeting/  [Biblioteka algorytmu retargetingu dłoni zręcznościowej]
│   │      │                         Retargeting = mapowanie ruchów ludzkiej dłoni na robota
│   │      ├── robot_arm_ik.py       [Odwrotna kinematyka dla ramienia]
│   │      │                         IK (Inverse Kinematics) = obliczanie kątów stawów
│   │      │                         potrzebnych do osiągnięcia docelowej pozycji
│   │      ├── robot_arm.py          [Steruje stawami obu ramion i blokuje inne części]
│   │      ├── hand_retargeting.py   [Wrapper dla biblioteki retargetingu dłoni zręcznościowej]
│   │      ├── robot_hand_inspire.py [Steruje dłonią zręcznościową Inspire]
│   │      ├── robot_hand_unitree.py [Steruje dłonią zręcznościową Unitree]
│   │
│   ├── utils/
│   │      ├── episode_writer.py          [Używany do nagrywania danych dla uczenia imitacyjnego]
│   │      │                              Imitation Learning = uczenie robota przez pokazywanie
│   │      ├── weighted_moving_filter.py  [Filtr dla danych stawów]
│   │      │                              Wygładza ruchy, usuwa szum
│   │      ├── rerun_visualizer.py        [Wizualizuje nagrane dane]
│   │      ├── ipc.py                     [Obsługuje komunikację międzyprocesową z programami proxy]
│   │      ├── motion_switcher.py         [Przełącza stany sterowania ruchem]
│   │      ├── sim_state_topic.py         [Do wdrożenia symulacyjnego]
│   │
│   └── teleop_hand_and_arm.py    [Skrypt startowy dla teleoperation]
│                                 To główny plik, który uruchamiasz!

```

## Główne komponenty systemu

### 1. teleimager (Usługa Obrazu)
**Co robi:** Zbiera obraz z kamer robota i przesyła go do gogli VR.
**Kluczowe funkcje:**
- Kompresja wideo
- Transmisja przez WebRTC lub inne protokoły
- Obsługa wielu kamer jednocześnie

### 2. televuer (Interfejs XR)
**Co robi:** Łączy się z goglami VR/AR i śledzi Twoje ruchy.
**Kluczowe funkcje:**
- Śledzenie pozycji głowy
- Śledzenie pozycji rąk lub kontrolerów
- Wyświetlanie widoku robota w googlach

### 3. robot_control (Sterowanie Robotem)
**Co robi:** Tłumaczy Twoje ruchy na komendy dla robota.
**Kluczowe komponenty:**
- **IK (Inverse Kinematics)**: Oblicza jakie kąty stawów potrzebne są aby ramię dotarło do określonej pozycji
- **Retargeting**: Mapuje ruchy ludzkiej dłoni na dłoń zręcznościową robota
- **Kontrolery**: Wysyłają komendy do motorów robota

### 4. utils (Narzędzia Pomocnicze)
**Co robi:** Dostarcza dodatkowe funkcje wspierające główny system.
**Kluczowe narzędzia:**
- **episode_writer**: Nagrywa dane do późniejszego treningu AI
- **filtry**: Wygładzają ruchy, usuwają szum z danych sensorów
- **IPC**: Komunikacja z innymi programami


# 5. 🛠️ Sprzęt

Szczegółowe informacje o wymaganym sprzęcie znajdziesz w [dokumencie Device_pl.md](Device_pl.md).



# 6. 🙏 Podziękowania

Ten kod bazuje na następujących projektach open-source. Odwiedź poniższe URL, aby zapoznać się z odpowiednimi licencjami:

1. https://github.com/OpenTeleVision/TeleVision
2. https://github.com/dexsuite/dex-retargeting
3. https://github.com/vuer-ai/vuer
4. https://github.com/stack-of-tasks/pinocchio
5. https://github.com/casadi/casadi
6. https://github.com/meshcat-dev/meshcat-python
7. https://github.com/zeromq/pyzmq
8. https://github.com/Dingry/BunnyVisionPro
9. https://github.com/unitreerobotics/unitree_sdk2_python
10. https://github.com/ARCLab-MIT/beavr-bot

---

## 📚 Dalsze kroki w nauce

Teraz gdy znasz już podstawy, możesz:

1. **Eksperymentować w symulacji** - Bezpieczne środowisko do nauki
2. **Czytać kod źródłowy** - Najlepszy sposób na głębsze zrozumienie
3. **Dołączyć do społeczności** - [Discord](https://discord.gg/ZwcVwxv5rq) i [Wiki](https://github.com/unitreerobotics/xr_teleoperate/wiki)
4. **Zbierać dane treningowe** - Dla projektów uczenia maszynowego
5. **Modyfikować i ulepszać** - Projekt jest open-source!

## ❓ Pomoc i wsparcie

Jeśli masz pytania:
- Sprawdź [Wiki](https://github.com/unitreerobotics/xr_teleoperate/wiki)
- Dołącz do [Discord](https://discord.gg/ZwcVwxv5rq)
- Przeczytaj [Issues na GitHubie](https://github.com/unitreerobotics/xr_teleoperate/issues)
- Skonsultuj się z [oficjalną dokumentacją Unitree](https://support.unitree.com/)

**Powodzenia w Twojej przygodzie z robotypką! 🤖✨**