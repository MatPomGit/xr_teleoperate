# Opis robota Unitree H1 (URDF & MJCF)

## Przegląd

Ten pakiet zawiera uproszczony opis robota (URDF & MJCF) dla [Unitree H1](https://www.unitree.com/h1/), opracowany przez [Unitree Robotics](https://www.unitree.com/).

<p align="center">
  <img src="h1_2.png" width="500"/>
</p>

## O robocie Unitree H1

Robot Unitree H1 to zaawansowany robot humanoidalny o 51 stopniach swobody (DoF):

### Czym jest "stopień swobody" (DoF)?

**DoF (Degree of Freedom)** = sposób, w jaki część robota może się poruszać:
- 1 DoF = może poruszać się w jednym kierunku (np. łokieć zgina się tylko w jednej płaszczyźnie)
- 3 DoF = może poruszać się w trzech kierunkach (np. ramię w stawie barkowym)

**51 DoF robota H1 oznacza 51 niezależnych ruchów**, które robot może wykonać!

## Szczegółowa struktura kinematyczna robota H1

Poniżej znajduje się kompletne drzewo stawów robota pokazujące wszystkie 51 stopni swobody:

```text
korzeń [⚓] => /miednica/
    left_hip_yaw_joint [⚙+Z] => /left_hip_yaw_link/
        left_hip_pitch_joint [⚙+Y] => /left_hip_pitch_link/
            left_hip_roll_joint [⚙+X] => /left_hip_roll_link/
                left_knee_joint [⚙+Y] => /left_knee_link/
                    left_ankle_pitch_joint [⚙+Y] => /left_ankle_pitch_link/
                        left_ankle_roll_joint [⚙+X] => /left_ankle_roll_link/
    right_hip_yaw_joint [⚙+Z] => /right_hip_yaw_link/
        right_hip_pitch_joint [⚙+Y] => /right_hip_pitch_link/
            right_hip_roll_joint [⚙+X] => /right_hip_roll_link/
                right_knee_joint [⚙+Y] => /right_knee_link/
                    right_ankle_pitch_joint [⚙+Y] => /right_ankle_pitch_link/
                        right_ankle_roll_joint [⚙+X] => /right_ankle_roll_link/
    torso_joint [⚙+Z] => /torso_link/
        left_shoulder_pitch_joint [⚙+Y] => /left_shoulder_pitch_link/
            left_shoulder_roll_joint [⚙+X] => /left_shoulder_roll_link/
                left_shoulder_yaw_joint [⚙+Z] => /left_shoulder_yaw_link/
                    left_elbow_pitch_joint [⚙+Y] => /left_elbow_pitch_link/
                        left_elbow_roll_joint [⚙+X] => /left_elbow_roll_link/
                            left_wrist_pitch_joint [⚙+Y] => /left_wrist_pitch_link/
                                left_wrist_yaw_joint [⚙+Z] => /left_wrist_yaw_link/
                                    L_base_link_joint [⚓] => /L_hand_base_link/
                                        L_thumb_proximal_yaw_joint [⚙+Z] => /L_thumb_proximal_base/
                                            L_thumb_proximal_pitch_joint [⚙-Z] => /L_thumb_proximal/
                                                L_thumb_intermediate_joint [⚙-Z] => /L_thumb_intermediate/
                                                    L_thumb_distal_joint [⚙-Z] => /L_thumb_distal/
                                        L_index_proximal_joint [⚙-Z] => /L_index_proximal/
                                            L_index_intermediate_joint [⚙-Z] => /L_index_intermediate/
                                        L_middle_proximal_joint [⚙-Z] => /L_middle_proximal/
                                            L_middle_intermediate_joint [⚙-Z] => /L_middle_intermediate/
                                        L_ring_proximal_joint [⚙-Z] => /L_ring_proximal/
                                            L_ring_intermediate_joint [⚙-Z] => /L_ring_intermediate/
                                        L_pinky_proximal_joint [⚙-Z] => /L_pinky_proximal/
                                            L_pinky_intermediate_joint [⚙-Z] => /L_pinky_intermediate/
        right_shoulder_pitch_joint [⚙+Y] => /right_shoulder_pitch_link/
            right_shoulder_roll_joint [⚙+X] => /right_shoulder_roll_link/
                right_shoulder_yaw_joint [⚙+Z] => /right_shoulder_yaw_link/
                    right_elbow_pitch_joint [⚙+Y] => /right_elbow_pitch_link/
                        right_elbow_roll_joint [⚙+X] => /right_elbow_roll_link/
                            right_wrist_pitch_joint [⚙+Y] => /right_wrist_pitch_link/
                                right_wrist_yaw_joint [⚙+Z] => /right_wrist_yaw_link/
                                    R_base_link_joint [⚓] => /R_hand_base_link/
                                        R_thumb_proximal_yaw_joint [⚙-Z] => /R_thumb_proximal_base/
                                            R_thumb_proximal_pitch_joint [⚙+Z] => /R_thumb_proximal/
                                                R_thumb_intermediate_joint [⚙+Z] => /R_thumb_intermediate/
                                                    R_thumb_distal_joint [⚙+Z] => /R_thumb_distal/
                                        R_index_proximal_joint [⚙+Z] => /R_index_proximal/
                                            R_index_intermediate_joint [⚙+Z] => /R_index_intermediate/
                                        R_middle_proximal_joint [⚙+Z] => /R_middle_proximal/
                                            R_middle_intermediate_joint [⚙+Z] => /R_middle_intermediate/
                                        R_ring_proximal_joint [⚙+Z] => /R_ring_proximal/
                                            R_ring_intermediate_joint [⚙+Z] => /R_ring_intermediate/
                                        R_pinky_proximal_joint [⚙+Z] => /R_pinky_proximal/
                                            R_pinky_intermediate_joint [⚙+Z] => /R_pinky_intermediate/
```

### Legenda symboli:
- **[⚓]** = Stały link (nie porusza się)
- **[⚙+X]** = Staw obrotowy wokół osi X (dodatni kierunek)
- **[⚙+Y]** = Staw obrotowy wokół osi Y (dodatni kierunek)
- **[⚙+Z]** = Staw obrotowy wokół osi Z (dodatni kierunek)
- **[⚙-X/-Y/-Z]** = Staw obrotowy w ujemnym kierunku

### Rozkład stopni swobody:

**Nogi (12 DoF na obie):**
- 6 DoF na każdą nogę
- Biodro: 3 DoF (yaw, pitch, roll)
- Kolano: 1 DoF (pitch)
- Kostka: 2 DoF (pitch, roll)

**Ramiona (14 DoF na oba):**
- 7 DoF na każde ramię
- Ramię: 3 DoF (pitch, roll, yaw)
- Łokieć: 2 DoF (pitch, roll)
- Nadgarstek: 2 DoF (pitch, yaw)

**Dłonie (20 DoF na obie):**
- 10 DoF na każdą dłoń
- Kciuk: 4 DoF
- Palec wskazujący: 2 DoF
- Palec środkowy: 2 DoF
- Palec serdeczny: 2 DoF
- Mały palec: 2 DoF

**Tułów (1 DoF):**
- Obrót wokół osi pionowej

**Głowa (4 DoF):**
- Pochylenie, obrót, przechylenie, wysuw

**Razem: 12 + 14 + 20 + 1 + 4 = 51 DoF!**

## Wizualizacja z [MuJoCo](https://github.com/google-deepmind/mujoco)

### Jak uruchomić wizualizację:

1. **Instalacja MuJoCo:**

   ```bash
   pip install mujoco
   ```

2. **Otwórz przeglądarkę MuJoCo:**

   ```bash
   python -m mujoco.viewer
   ```

3. **Załaduj model sceny:**
   - Przeciągnij i upuść plik modelu MJCF (`scene.xml`) do okna przeglądarki MuJoCo
   - Model się załaduje z robotem i środowiskiem

### Co zawiera plik scene.xml?

Plik `scene.xml` zawiera:
- **Kompletny model robota H1** z wszystkimi stawami
- **Środowisko symulacyjne** (podłoga, oświetlenie)
- **Parametry fizyczne** (grawitacja, tarcie)
- **Opcje renderowania** (kamery, shadery)

### Wskazówki dotyczące sterowania w przeglądarce MuJoCo:
- **Lewy przycisk myszy + ruch** = Obróć kamerę wokół robota
- **Prawy przycisk myszy + ruch** = Przesuń widok
- **Scroll myszy** = Przybliż/Oddal
- **Spacja** = Włącz/Wyłącz symulację fizyki
- **Ctrl+R** = Zresetuj symulację do pozycji początkowej
- **Tab** = Przełącz między trybami edycji
- **Backspace** = Wyłącz symulację

### Eksperymentowanie z robotem:
1. **Włącz symulację (Spacja)** - robot zacznie reagować na grawitację
2. **Klikaj na stawy** - zobaczysz ich właściwości
3. **Zastosuj siły** - Ctrl+klik i przeciągnij aby aplikować siły
4. **Zmień parametry** - Edytuj scene.xml aby zmienić właściwości fizyczne

## Różnice między H1 a H1_2

**H1_2** to ulepszona wersja robota H1:
- **Ramiona 7-DoF zamiast 4-DoF** - większa zręczność i możliwości manipulacji
- **Lepsze dłonie zręcznościowe** - więcej stopni swobody w palcach
- **Ulepszona kinematyka** - płynniejsze i bardziej naturalne ruchy
- **Optymalizacja dla teleoperation** - lepsze śledzenie ruchów człowieka

## Pliki w tym katalogu

- **h1_2.urdf** - Opis robota w formacie URDF (dla ROS i innych narzędzi)
- **h1_2.xml** - Model robota w formacie MJCF (tylko robot)
- **scene.xml** - Kompletna scena symulacyjna z robotem i środowiskiem
- **meshes/** - Katalog z plikami geometrii 3D (modele STL/OBJ)

## Zastosowania

### Dla teleoperation:
- Plik `h1_2.urdf` jest używany przez moduł `robot_arm_ik.py` do obliczeń kinematyki odwrotnej
- Określa dokładne pozycje i orientacje wszystkich stawów
- Definiuje limity ruchów dla bezpieczeństwa

### Dla symulacji:
- Plik `scene.xml` jest używany przez symulator Isaac Lab
- Umożliwia testowanie algorytmów sterowania bez fizycznego robota
- Pozwala na szybkie prototypowanie i debugowanie

### Dla wizualizacji:
- Wszystkie pliki mogą być używane do wizualizacji w różnych narzędziach
- Przydatne do planowania trajektorii i analiz kinematycznych
- Pomaga w zrozumieniu struktury robota

## Modyfikowanie modelu

Jeśli chcesz zmodyfikować model robota:

1. **Kopia zapasowa** - Zawsze zrób kopię oryginalnego pliku
2. **Edycja XML** - Otwórz plik w edytorze tekstu
3. **Dokumentacja formatów:**
   - [URDF Specification](http://wiki.ros.org/urdf/XML)
   - [MJCF Documentation](https://mujoco.readthedocs.io/en/stable/XMLreference.html)
4. **Walidacja** - Sprawdź poprawność składni przed użyciem
5. **Testowanie** - Załaduj zmodyfikowany model w przeglądarce MuJoCo

### Często modyfikowane parametry:
- **Limity stawów** - maksymalne i minimalne kąty
- **Prędkości maksymalne** - jak szybko stawy mogą się poruszać
- **Masy** - wpływa na dynamikę i bezwładność
- **Geometrie kolizji** - uproszczone kształty do wykrywania kolizji

## Dodatkowe zasoby

- [Oficjalna dokumentacja Unitree H1](https://support.unitree.com/home/en/H1_developer)
- [Specyfikacja techniczna H1](https://www.unitree.com/h1/)
- [Dokumentacja MuJoCo](https://mujoco.readthedocs.io/)
- [Tutoriale URDF](http://wiki.ros.org/urdf/Tutorials)

## Często zadawane pytania (FAQ)

**P: Dlaczego robot ma tak wiele stopni swobody?**
O: Aby móc wykonywać złożone, naturalne ruchy podobne do ludzkich. Więcej DoF = większa zręczność.

**P: Czy mogę użyć tego modelu w Unity lub Unreal Engine?**
O: Tak, ale musisz przekonwertować URDF na format obsługiwany przez te silniki (FBX, COLLADA). Są dostępne narzędzia do konwersji.

**P: Jak znaleźć właściwości fizyczne (masy, bezwładności)?**
O: Są one zawarte w plikach URDF/MJCF w tagach `<mass>` i `<inertia>`. Zobacz dokumentację formatów.

**P: Czy model zawiera tekstury i materiały?**
O: Tak, są one referencjonowane w plikach mesh. Upewnij się, że masz katalog meshes/ w tej samej lokalizacji.

**P: Model nie ładuje się poprawnie, co robić?**
O: Sprawdź:
1. Czy wszystkie pliki mesh są w odpowiednim miejscu
2. Czy ścieżki w XML/URDF są prawidłowe
3. Czy używasz kompatybilnej wersji MuJoCo/parsera URDF
4. Logi błędów mogą wskazać problem
