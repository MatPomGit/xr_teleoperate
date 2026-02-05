# 5. 🛠️ Sprzęt - Kompletny przewodnik dla początkujących

## Wprowadzenie do wymaganego sprzętu

Ten dokument opisuje szczegółowo sprzęt potrzebny do uruchomienia systemu teleoperation dla robotów Unitree. Jeśli dopiero zaczynasz, ta sekcja pomoże Ci zrozumieć:
- **Jaki sprzęt jest absolutnie niezbędny** (bez niego system nie zadziała)
- **Jaki sprzęt jest opcjonalny** (przydatny dla zaawansowanych zastosowań)
- **Gdzie kupić** poszczególne komponenty
- **Jak je zamontować** na robocie

## 5.1 🎮 Urządzenia do teleoperation (WYMAGANE)

> **Te elementy są absolutnie konieczne do uruchomienia podstawowego systemu teleoperation.**

<table border="1" cellspacing="0" cellpadding="5" style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Element</th>
    <th style="text-align: center;">Ilość</th>
    <th style="text-align: center;">Specyfikacja</th>
    <th style="text-align: center;">Uwagi</th>
  </tr>
  <tr>
    <td style="text-align: center;"><b>Robot humanoidalny Unitree G1</b></td>
    <td style="text-align: center;">1</td>
    <td style="text-align: center;"><a href="https://www.unitree.com/cn/g1">https://www.unitree.com/cn/g1</a></td>
    <td style="text-align: center;">
      <b>Wymagana wersja z jednostką obliczeniową dla deweloperów</b><br>
      To wersja robota, która posiada dodatkowy komputer wbudowany (PC2),<br>
      na którym można uruchamiać własne programy.
    </td>
  </tr>
  <tr>
    <td style="text-align: center;"><b>Urządzenie XR (gogle VR/AR)</b></td>
    <td style="text-align: center;">1</td>
    <td style="text-align: center;">
      <a href="https://www.apple.com.cn/apple-vision-pro/">Apple Vision Pro</a><br />
      <a href="https://www.picoxr.com/products/pico4-ultra-enterprise">PICO 4 Ultra Enterprise</a><br />
      <a href="https://www.meta.com/quest/quest-3">Meta Quest 3</a><br />
      <a href="https://www.meta.com/quest/quest-3s/">Meta Quest 3S</a><br />
    </td>
    <td style="text-align: center;">
      <b>Wybierz jedno z tych urządzeń</b><br>
      <a href="https://github.com/unitreerobotics/xr_teleoperate/wiki/XR_Device">Sprawdź nasze Wiki [XR_Device] dla szczegółów</a><br><br>
      <b>Co to jest XR?</b><br>
      XR (Extended Reality) to ogólna nazwa dla urządzeń VR/AR/MR.<br>
      Używasz ich do sterowania robotem i widzenia z jego perspektywy.
    </td>
  </tr>
  <tr>
    <td style="text-align: center;"><b>Router WiFi</b></td>
    <td style="text-align: center;">1</td>
    <td style="text-align: center;">
      <b>Zalecane: przynajmniej wsparcie WiFi6</b><br>
      WiFi 6 zapewnia niższe opóźnienia i wyższą przepustowość<br>
      niezbędne dla płynnego sterowania w czasie rzeczywistym
    </td>
    <td style="text-align: center;">
      <b>Wymagany w trybie przewodowym</b> (robot podłączony kablem)<br>
      <b>Opcjonalny w trybie bezprzewodowym</b><br><br>
      <b>Dlaczego potrzebujemy routera?</b><br>
      Router tworzy lokalną sieć łączącą:<br>
      - Twój komputer Host<br>
      - Komputer robota (PC2)<br>
      - Gogle XR
    </td>
  </tr>
  <tr>
    <td style="text-align: center;"><b>Komputer użytkownika (Host)</b></td>
    <td style="text-align: center;">1</td>
    <td style="text-align: center;">
      <b>Zalecane:</b><br>
      - Architektura x86-64<br>
      - Ubuntu 20.04 lub 22.04<br>
      - Co najmniej 8GB RAM<br>
      - Procesor wielordzeniowy
    </td>
    <td style="text-align: center;">
      <b>Dla trybu symulacji</b> postępuj zgodnie z<br>
      <a href="https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/requirements.html">oficjalnymi zaleceniami sprzętowymi NVIDIA</a><br><br>
      <b>Co robi ten komputer?</b><br>
      - Uruchamia główny program sterujący<br>
      - Przetwarza dane z gogli XR<br>
      - Wysyła komendy do robota
    </td>
  </tr>
  <tr>
    <td style="text-align: center;"><b>Kamera głowy</b></td>
    <td style="text-align: center;">1</td>
    <td style="text-align: center;">
      <b>Opcja 1: Kamera monokularna</b> (wbudowana Realsense D435i)<br />
      <b>Opcja 2: Kamera stereo</b> (montaż zewnętrzny, szczegóły w rozdziale 5.2)
    </td>
    <td style="text-align: center;">
      <b>Używana do widoku z perspektywy głowy robota</b><br>
      Kamera stereo zapewnia większe poczucie głębi i immersji.<br><br>
      <b>Czym się różnią?</b><br>
      - Monokularna = jeden obiektyw (jak jedno oko)<br>
      - Stereo = dwa obiektywy (jak dwa oczy, obraz 3D)<br><br>
      Obsługiwana przez <a href="https://github.com/unitreerobotics/xr_teleoperate/tree/main/teleop/image_server">image_server</a>
    </td>
  </tr>
  <tr>
    <td style="text-align: center;"><b>Kabel USB3.0</b></td>
    <td style="text-align: center;">1</td>
    <td style="text-align: center;">
      Type-C podwójne proste złącza, około 0.2m długości
    </td>
    <td style="text-align: center;">
      Do podłączenia kamery stereo głowy<br><br>
      <b>Dlaczego USB 3.0?</b><br>
      Kamery przesyłają dużo danych wideo -<br>
      USB 3.0 ma wystarczającą przepustowość
    </td>
  </tr>
</table>


## 5.2 💽 Urządzenia do zbierania danych (OPCJONALNE)

> **Te elementy są opcjonalne. Są potrzebne tylko jeśli chcesz nagrywać wysokiej jakości [zestawy danych](https://huggingface.co/unitreerobotics) do uczenia maszynowego.**
>
> **Parametry, linki itp. są tylko dla referencji.**

### Czym jest zbieranie danych i dlaczego jest ważne?

**Zbieranie danych** (data collection) to proces nagrywania działań robota podczas gdy Ty go sterujesz. Te nagrania można później użyć do:
- **Uczenia maszynowego** - nauczenia AI jak wykonywać zadania autonomicznie
- **Analizy** - badania jak robot wykonuje różne ruchy
- **Dokumentacji** - zapisania procedur dla innych

### 5.2.1 Kamera stereo 60 FPS (wyższa jakość)

**Dlaczego 60 FPS jest lepsze od 30 FPS?**
- Płynniejszy obraz (więcej klatek na sekundę)
- Lepsze dla szybkich ruchów
- Wyższa jakość danych treningowych

#### Materiały potrzebne

> W porównaniu z kamerą z sekcji 5.2.2, ta zwiększa częstotliwość klatek z 30 FPS do 60 FPS i ma inne wymiary montażowe.

|       Element        | Ilość |                        Specyfikacja                         |                           Uwagi                            |
| :---------------: | :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| Kamera stereo RGB |    1     | [60FPS, 125°FOV, 60mm baseline](https://e.tb.cn/h.S2zMNwiUzC9I2H1) |                  Do perspektywy głowy robota<br><br><b>Parametry wyjaśnione:</b><br>- 60FPS = 60 klatek/sekundę<br>- 125° FOV = szeroki kąt widzenia<br>- 60mm baseline = odległość między obiektywami                  |
|  Śruby M4x16mm   |    2     |           [Referencja](https://amzn.asia/d/cfta55x)           |                 Do mocowania wspornika kamery                 |
| Śruby M2x5mm/6mm |    8     |           [Referencja](https://amzn.asia/d/1msRa5B)           | Do mocowania (kamera - wspornik kamery) i (wspornik kamery - pokrywa kamery) |

#### Części do druku 3D

**Co to jest druk 3D?**
Niektóre komponenty montażowe musisz sam wydrukować na drukarce 3D. Pliki STL/STEP są dostarczone - możesz je pobrać i wydrukować lokalnie lub zlecić drukowanie firmie.

<table border="1" cellspacing="0" cellpadding="5" style="border-collapse: collapse; width: 100%; text-align: center;">
  <colgroup>
    <col style="width: 20%;">
    <col style="width: 20%;">
    <col style="width: 20%;">
    <col style="width: 20%;">
    <col style="width: 20%;">
  </colgroup>
  <tr>
    <th>Element</th>
    <th>Wspornik kamery</th>
    <th>Pokrywa kamery</th>
    <th>Zacisk USB-Type-C</th>
    <th>Link do pobrania</th>
  </tr>
  <tr>
    <td>
      <img src="https://oss-global-cdn.unitree.com/static/e5ca0cc978cb4b48b693869bbc0e2a36_1023x885.png" style="max-width:45%; margin-bottom:5px;"/><br />
      <b>Klasyczna głowa (98mm)</b><br>
      Starsza wersja głowy robota G1
    </td>
    <td><img src="https://oss-global-cdn.unitree.com/static/d8b0d8faa2d94a84a292bc4c26c65f2a_1920x1080.png" style="max-width:100%;"/></td>
    <td><img src="https://oss-global-cdn.unitree.com/static/caa6e17e8fba45b1a53c9109e9a6a9a4_1509x849.png" style="max-width:50%;"/></td>
    <td align="center"><img src="https://oss-global-cdn.unitree.com/static/ea8edf0b4dd54ea792935eee9b70f550_1443x641.png" style="max-width:30%;"/></td>
    <td><a href="https://oss-global-cdn.unitree.com/static/477103c571dc46f99ec6e0b57b3b3be6.zip">📥 Części do druku 3D - Klasyczna</a></td>
  </tr>
  <tr>
    <td>
      <img src="https://oss-global-cdn.unitree.com/static/af9f379642e044bc9e88040b2c33a4c4_1110x904.png" style="max-width:50%; margin-bottom:5px;"/><br />
      <b>Odnowiona głowa (88mm)</b><br>
      Nowsza wersja głowy robota G1
    </td>
    <td><img src="https://oss-global-cdn.unitree.com/static/d8b0d8faa2d94a84a292bc4c26c65f2a_1920x1080.png" style="max-width:100%;"/></td>
    <td><img src="https://oss-global-cdn.unitree.com/static/caa6e17e8fba45b1a53c9109e9a6a9a4_1509x849.png" style="max-width:50%;"/></td>
    <td align="center"><img src="https://oss-global-cdn.unitree.com/static/ea8edf0b4dd54ea792935eee9b70f550_1443x641.png" style="max-width:30%;"/></td>
    <td><a href="https://oss-global-cdn.unitree.com/static/950f53b95d5943589e278241b59c86ff.zip">📥 Części do druku 3D - Odnowiona</a></td>
  </tr>
</table>

**Jak sprawdzić którą wersję głowy masz?**
Zmierz szerokość głowy robota - klasyczna jest szersza (98mm), odnowiona węższa (88mm).

### 5.2.2 Kamera stereo 30 FPS (standardowa)

**Kiedy wybrać tę opcję?**
- Niższy koszt
- Wystarczająca dla większości zastosowań
- Prostszy montaż

#### Materiały potrzebne

|       Element        | Ilość |                        Specyfikacja                         |                           Uwagi                            |
| :---------------: | :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|   Kamera stereo   |    1     | [30FPS, 125°FOV, 60mm baseline](http://e.tb.cn/h.TaZxgkpfWkNCakg) |                  Do perspektywy głowy robota                  |
|  Śruby M4x16mm   |    2     |           [Referencja](https://amzn.asia/d/cfta55x)           |                 Do mocowania wspornika kamery                 |
| Śruby M2x5mm/6mm |    8     |           [Referencja](https://amzn.asia/d/1msRa5B)           | Do mocowania (kamera - wspornik kamery) i (wspornik kamery - pokrywa kamery) |

#### Części do druku 3D

<table border="1" cellspacing="0" cellpadding="5" style="border-collapse: collapse; width: 100%; text-align: center;">
  <colgroup>
    <col style="width: 20%;">
    <col style="width: 25%;">
    <col style="width: 25%;">
    <col style="width: 30%;">
  </colgroup>
  <tr>
    <th>Element</th>
    <th>Wspornik kamery</th>
    <th>Pokrywa kamery</th>
    <th>Link do pobrania</th>
  </tr>
  <tr>
    <td>
      <img src="https://oss-global-cdn.unitree.com/static/e5ca0cc978cb4b48b693869bbc0e2a36_1023x885.png" style="max-width:45%; margin-bottom:5px;"/><br />
      <b>Klasyczna głowa (98mm)</b>
    </td>
    <td><img src="https://oss-global-cdn.unitree.com/static/d8b0d8faa2d94a84a292bc4c26c65f2a_1920x1080.png" style="max-width:100%;"/></td>
    <td>Brak</td>
    <td><a href="https://oss-global-cdn.unitree.com/static/39dea40900784b199bcba31e72c906b9.zip">📥 Części do druku 3D - Klasyczna</a></td>
  </tr>
  <tr>
    <td>
      <img src="https://oss-global-cdn.unitree.com/static/af9f379642e044bc9e88040b2c33a4c4_1110x904.png" style="max-width:50%; margin-bottom:5px;"/><br />
      <b>Odnowiona głowa (88mm)</b>
    </td>
    <td><img src="https://oss-global-cdn.unitree.com/static/d8b0d8faa2d94a84a292bc4c26c65f2a_1920x1080.png" style="max-width:100%;"/></td>
    <td><img src="https://oss-global-cdn.unitree.com/static/caa6e17e8fba45b1a53c9109e9a6a9a4_1509x849.png" style="max-width:50%;"/></td>
    <td><a href="https://oss-global-cdn.unitree.com/static/58e300cc99da48f4a4977998c48cefa3.zip">📥 Części do druku 3D - Odnowiona</a></td>
  </tr>
</table>

### 5.2.3 Kamery nadgarstka - RealSense D405 (dla G1)

**Co to są kamery nadgarstka i po co są?**
Kamery nadgarstka są montowane na nadgarstkach robota (przy dłoniach) i zapewniają:
- **Widok z bliska** - robot widzi dokładnie co manipuluje
- **Percepcję głębi** - RealSense to kamery 3D z czujnikiem głębi
- **Lepsze dane treningowe** - AI widzi szczegóły manipulowanych obiektów

> RealSense D405 jest zalecana **tylko dla efektora końcowego [Unitree Dex3-1](https://www.unitree.com/Dex3-1)**.

#### Materiały potrzebne

|      Element      | Ilość |                        Specyfikacja                         |                           Uwagi                            |
| :------------: | :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| RealSense D405 |    2     | [Strona internetowa](https://www.intelrealsense.com/depth-camera-d405/) | Dla lewego i prawego nadgarstka robota G1 (silniki M4010)<br><br><b>Dlaczego dwie?</b><br>Robot ma dwie ręce, więc potrzebujemy dwóch kamer!  |
|   Hub USB3.0   |    1     | [Problem](https://github.com/IntelRealSense/librealsense/issues/24) | Wybierz wysokiej jakości hub; zalecane podłączenie do [Type-C #9](https://support.unitree.com/home/en/G1_developer/about_G1)<br><br><b>Po co hub?</b><br>Dwie kamery = dwa porty USB. Hub pozwala podłączyć obie do jednego portu komputera. |
|  Nakrętka M3-1  |    4     |             [Referencja](https://a.co/d/gQaLtHD)              |                     Do mocowania nadgarstka                      |
|  Śruba M3x12   |    4     |           [Referencja](https://amzn.asia/d/aU9NHSf)           |                     Do mocowania nadgarstka                      |
|   Śruba M3x6   |    4     |           [Referencja](https://amzn.asia/d/0nEz5dJ)           |                     Do mocowania nadgarstka                      |

#### Części do druku 3D

|           Element           | Ilość |            Uwagi             |                        Link do pobrania                         |
| :----------------------: | :------: | :----------------------------: | :----------------------------------------------------------: |
|     Pierścień nadgarstka D405      |    2     |  Do użytku ze wspornikiem nadgarstka   | [📥 STEP](https://github.com/unitreerobotics/xr_teleoperate/blob/7cd188c1657ad4df97cfcd44e9f35bac937f7f2b/hardware/wrist_ring_mount.STEP) |
| Wspornik kamery lewego nadgarstka  |    1     | Do montażu lewej kamery D405  | [📥 STEP](https://github.com/unitreerobotics/xr_teleoperate/blob/7cd188c1657ad4df97cfcd44e9f35bac937f7f2b/hardware/left_wrist_D405_camera_mount.STEP) |
| Wspornik kamery prawego nadgarstka |    1     | Do montażu prawej kamery D405 | [📥 STEP](https://github.com/unitreerobotics/xr_teleoperate/blob/7cd188c1657ad4df97cfcd44e9f35bac937f7f2b/hardware/right_wrist_D405_camera_mount.STEP) |

### 5.2.4 Kamery nadgarstka - Kamera monokularna (dla G1)

**Kiedy wybrać kamery monokularne zamiast RealSense?**
- Niższy koszt
- Wyższa częstotliwość klatek (60 FPS)
- Szerszy kąt widzenia (160°)
- Brak danych głębi (tylko obraz 2D)

#### Materiały potrzebne

|       Element        | Ilość |                        Specyfikacja                         |                      Uwagi                       |
| :---------------: | :------: | :----------------------------------------------------------: | :------------------------------------------------: |
| Kamera monokularna  |    2     | [60FPS, 160° FOV](https://e.tb.cn/h.S2YWUJan6ZP8Wqv?tk=MqHK4uvWlLk) |   Dla lewego i prawego nadgarstka robota G1 (silniki M4010)   |
|    Hub USB3.0     |    1     | [Referencja](https://e.tb.cn/h.S2QB8hVuKbNfqb9?tk=XsBL4uwn2Ch) |          Do podłączenia dwóch kamer nadgarstka          |
|   Nakrętka M3-1    |    4     |             [Referencja](https://a.co/d/gQaLtHD)              |                Do mocowania nadgarstka                 |
|    Śruba M3x12    |    4     |           [Referencja](https://amzn.asia/d/aU9NHSf)           |         Do mocowania wspornika i pierścienia nadgarstka         |
|   Śruba M2.5x5    |    4     |           [Referencja](https://amzn.asia/d/0nEz5dJ)           |     Do mocowania zacisku kabla i wspornika nadgarstka     |
| Śruby M2x5mm/6mm |    8     |           [Referencja](https://amzn.asia/d/1msRa5B)           | Do mocowania (kamera-wspornik) i (wspornik-pokrywa) |

#### Części do druku 3D

<table border="1" cellspacing="0" cellpadding="5" style="border-collapse: collapse; width: 100%; text-align: center;">
  <tr>
    <th>Efektor końcowy</th>
    <th>Wspornik kamery</th>
    <th>Pierścień nadgarstka</th>
    <th>Pokrywa kamery</th>
    <th>Zacisk kabla</th>
    <th>Link do pobrania</th>
  </tr>
  <tr>
    <td><a href="https://www.unitree.com/Dex1-1">Unitree Dex1-1</a><br>(Chwytaki)</td>
    <td><img src="https://oss-global-cdn.unitree.com/static/e21bd12e56b8442cb460aae93ca85443_1452x1047.png" width="120"/></td>
    <td><img src="https://oss-global-cdn.unitree.com/static/d867000b2cd6496595e5ca373b9e39a9_1133x683.png" width="120"/></td>
    <td><img src="https://oss-global-cdn.unitree.com/static/eb98c4f275db4d86b94e77746589cd94_1361x712.png" width="120"/></td>
    <td rowspan="3" valign="middle">
      <img src="https://oss-global-cdn.unitree.com/static/feefe9b679c34c5b8e88274174e23266_1095x689.png" width="120"/>
    </td>
    <td rowspan="3" valign="middle">
      <a href="https://oss-global-cdn.unitree.com/static/ff287f8f700948b5a30e3f4331a46b51.zip">📥 Pobierz części do druku 3D</a>
    </td>
  </tr>
  <tr>
    <td><a href="https://www.unitree.com/Dex3-1">Unitree Dex3-1</a><br>(Dłonie zręcznościowe)</td>
    <td><img src="https://oss-global-cdn.unitree.com/static/69e27c2433694c609f47f8c87265de90_893x741.png" width="120"/></td>
    <td><img src="https://oss-global-cdn.unitree.com/static/8d49682d9f4a49cdbcfba8660de88b81_982x588.png" width="120"/></td>
    <td><img src="https://oss-global-cdn.unitree.com/static/901421b01ca440d8bb8459feed1e42ff_1168x754.png" width="120"/></td>
  </tr>
  <tr>
    <td>
      <a href="https://support.unitree.com/home/en/G1_developer/inspire_dfx_dexterous_hand">Dłoń Inspire DFX</a> /
      <a href="https://support.unitree.com/home/en/G1_developer/brainco_hand">Dłoń Brainco</a><br>(Dłonie firm trzecich)
    </td>
    <td><img src="https://oss-global-cdn.unitree.com/static/b83d56bd28e64ccfb6c30bdcedfb536d_801x887.png" width="120"/></td>
    <td><img src="https://oss-global-cdn.unitree.com/static/763521d9313e4648b9dd23a3c11d8291_752x906.png" width="120"/></td>
    <td><img src="https://oss-global-cdn.unitree.com/static/68ed3a1ef0434801adbb73f2f45799e8_808x865.png" width="120"/></td>
  </tr>
</table>


## 5.3 🔨 Ilustracje montażu (przykłady)

**Wskazówki dotyczące montażu:**
1. **Przygotuj wszystkie części** przed rozpoczęciem montażu
2. **Sprawdź orientację** - upewnij się że montujesz we właściwym kierunku
3. **Nie dokręcaj zbyt mocno** - plastik z druku 3D może pęknąć
4. **Testuj po montażu** - sprawdź czy kamera jest stabilnie zamocowana

<table>
    <tr>
        <th align="center">Element</th>
        <th align="center" colspan="2">Symulacja/Demonstracja</th>
        <th align="center" colspan="2">Prawdziwe urządzenie</th>
    </tr>
    <tr>
        <td align="center"><b>Głowa</b></td>
        <td align="center">
            <p align="center">
                <img src="./img/head_camera_mount.png" alt="head" width="100%">
                <figcaption>Wspornik głowy</figcaption>
            </p>
        </td>
        <td align="center">
            <p align="center">
                <img src="./img/head_camera_mount_install.png" alt="head" width="80%">
                <figcaption>Widok z boku montażu</figcaption>
            </p>
        </td>
        <td align="center" colspan="2">
            <p align="center">
                <img src="./img/real_head.jpg" alt="head" width="20%">
                <figcaption>Widok z przodu montażu</figcaption>
            </p>
        </td>
    </tr>
    <tr>
        <td align="center"><b>Nadgarstek</b></td>
        <td align="center" colspan="2">
            <p align="center">
                <img src="./img/wrist_and_ring_mount.png" alt="wrist" width="100%">
                <figcaption>Pierścień nadgarstka i wspornik kamery</figcaption>
            </p>
        </td>
        <td align="center">
            <p align="center">
                <img src="./img/real_left_hand.jpg" alt="wrist" width="50%">
                <figcaption>Montaż lewej ręki</figcaption>
            </p>
        </td>
        <td align="center">
            <p align="center">
                <img src="./img/real_right_hand.jpg" alt="wrist" width="50%">
                <figcaption>Montaż prawej ręki</figcaption>
            </p>
        </td>
    </tr>
</table>


> **Uwaga:** Jak pokazano na czerwonych okręgach, wspornik pierścienia nadgarstka **musi być wyrównany ze szwem stawu nadgarstka**.
>
> **Dlaczego to ważne:**
> - Nieprawidłowe wyrównanie może powodować kolizje podczas ruchu
> - Kamera może być źle zorientowana
> - Mocowanie może być niestabilne

## 📋 Lista kontrolna zakupów

Aby ułatwić Ci zakupy, oto uproszczona lista kontrolna:

### Podstawowa konfiguracja (WYMAGANA):
- ☐ Robot Unitree G1 lub H1 (wersja developerska)
- ☐ Gogle XR (Apple Vision Pro / PICO 4 / Meta Quest 3)
- ☐ Router WiFi 6
- ☐ Komputer z Ubuntu 20.04/22.04
- ☐ Kabel USB3.0 Type-C

### Rozszerzona konfiguracja do zbierania danych (OPCJONALNA):
- ☐ Kamera stereo głowy (30 FPS lub 60 FPS)
- ☐ Kamery nadgarstka (RealSense D405 lub monokularne)
- ☐ Hub USB3.0
- ☐ Śruby montażowe (M2, M2.5, M3, M4)
- ☐ Nakrętki (M3-1)
- ☐ Dostęp do drukarki 3D (lub usługa druku)

## ❓ Często zadawane pytania (FAQ)

**P: Czy mogę użyć innych gogli VR niż wymienione?**
O: Teoretycznie tak, ale projekt jest testowany i optymalizowany dla wymienionych urządzeń. Inne mogą wymagać modyfikacji kodu.

**P: Czy muszę mieć kamery nadgarstka?**
O: Nie, są opcjonalne. System podstawowy działa bez nich, ale są bardzo przydatne dla zbierania danych do AI.

**P: Gdzie mogę wydrukować części 3D jeśli nie mam drukarki?**
O: Możesz użyć lokalnych usług druku 3D, bibliotek z drukarkami 3D, lub platform online jak 3DHubs.

**P: Jakie kolory/materiały użyć do druku 3D?**
O: Zalecamy:
- Materiał: PLA lub PETG (trwalsze)
- Wypełnienie: minimum 20%
- Kolor: dowolny, ale czarny jest najmniej widoczny

**P: Czy potrzebuję specjalnych uprawnień aby używać robota?**
O: Tak, zapoznaj się z lokalnym prawem dotyczącym robotów i zawsze przestrzegaj zasad bezpieczeństwa!

---

**Masz więcej pytań?** Sprawdź [Wiki](https://github.com/unitreerobotics/xr_teleoperate/wiki) lub dołącz do [Discord](https://discord.gg/ZwcVwxv5rq)!
