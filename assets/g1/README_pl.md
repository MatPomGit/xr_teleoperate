# Opis robota Unitree G1 (URDF & MJCF)

## Przegląd

Ten pakiet zawiera uniwersalny opis robota humanoidalnego (URDF & MJCF) dla [Unitree G1](https://www.unitree.com/g1/), opracowany przez [Unitree Robotics](https://www.unitree.com/).

### Czym są URDF i MJCF?

**URDF (Unified Robot Description Format)** - To format pliku XML opisujący:
- Strukturę kinematyczną robota (połączenia stawów)
- Geometrię wizualną (jak robot wygląda)
- Właściwości fizyczne (masy, bezwładności)
- Granice ruchu stawów

**MJCF (MuJoCo Model File)** - Format używany przez symulator MuJoCo:
- Podobny do URDF ale z dodatkowymi funkcjami dla symulacji
- Lepsze właściwości fizyczne i dynamika
- Używany w projektach z uczeniem maszynowym

## Dostępne pliki MJCF/URDF dla robota G1:

| Nazwa pliku MJCF/URDF           | `mode_machine` | Redukcja hip roll | Status aktualizacji | DoF#noga | DoF#talia | DoF#ramię | DoF#dłoń |
| ----------------------------- | :------------: | :----------------------: | ------------- | :-----: | :-------: | :-----: | :------: |
| `g1_23dof`                    |       1        |           14.5           | Beta          |   6*2   |     1     |   5*2   |    0     |
| `g1_29dof`                    |       2        |           14.5           | Beta          |   6*2   |     3     |   7*2   |    0     |
| `g1_29dof_with_hand`          |       2        |           14.5           | Beta          |   6*2   |     3     |   7*2   |   7*2    |
| `g1_29dof_lock_waist`         |       3        |           14.5           | Beta          |   6*2   |     1     |   7*2   |    0     |
| `g1_23dof_rev_1_0`            |       4        |           22.5           | Aktualne      |   6*2   |     1     |   5*2   |    0     |
| `g1_29dof_rev_1_0`            |       5        |           22.5           | Aktualne      |   6*2   |     3     |   7*2   |    0     |
| `g1_29dof_with_hand_rev_1_0`  |       5        |           22.5           | Aktualne      |   6*2   |     3     |   7*2   |   7*2    |
| `g1_29dof_lock_waist_rev_1_0` |       6        |           22.5           | Aktualne      |   6*2   |     1     |   7*2   |    0     |
| `g1_dual_arm`                 |       9        |           null           | Aktualne      |    0    |     0     |   7*2   |    0     |

### Wyjaśnienie skrótów:
- **DoF** (Degrees of Freedom) = Stopnie swobody, liczba niezależnych ruchów
- **6*2** = 6 stopni swobody na każdą nogę (łącznie 12)
- **7*2** = 7 stopni swobody na każde ramię (łącznie 14)
- **mode_machine** = Identyfikator konfiguracji sprzętowej
- **Beta** = Wersja testowa, może mieć niewielkie niedokładności
- **Aktualne** = Najnowsza, zweryfikowana wersja

### Który plik wybrać?

**Dla większości zastosowań teleoperation:**
- Użyj `g1_29dof_with_hand_rev_1_0` - najnowsza wersja z pełną funkcjonalnością

**Dla projektu xr_teleoperate:**
- `g1_body29_hand14` - specjalna wersja zmodyfikowana dla teleoperation

**Dla symulacji tylko ramion (bez nóg):**
- `g1_dual_arm` - zawiera tylko ramiona, szybsze obliczenia

## Wizualizacja z [MuJoCo](https://github.com/google-deepmind/mujoco)

MuJoCo to zaawansowany symulator fizyki używany w badaniach nad robotyką i AI.

### Jak uruchomić wizualizację:

1. **Instalacja MuJoCo:**

   ```bash
   pip install mujoco
   ```

2. **Otwórz przeglądarkę MuJoCo:**

   ```bash
   python -m mujoco.viewer
   ```

3. **Załaduj model:**
   - Przeciągnij i upuść plik modelu MJCF/URDF (`g1_XXX.xml` lub `g1_XXX.urdf`) do okna przeglądarki MuJoCo
   - Model się załaduje i będziesz mógł go obracać, zbliżać i symulować

### Wskazówki dotyczące wizualizacji:
- **Lewy przycisk myszy + przeciągnięcie** = Obróć widok
- **Prawy przycisk myszy + przeciągnięcie** = Przesuń widok
- **Scroll** = Przybliż/Oddal
- **Spacja** = Start/Stop symulacji
- **Ctrl+R** = Reset symulacji

## Uwaga dla teleoperation

**Ważne:** `g1_body29_hand14` jest zmodyfikowany z [g1_29dof_with_hand_rev_1_0](https://github.com/unitreerobotics/unitree_ros/blob/master/robots/g1_description/g1_29dof_with_hand_rev_1_0.urdf)

### Jakie modyfikacje zostały wprowadzone?
- Optymalizacja pod kątem teleoperation w czasie rzeczywistym
- Dostosowanie parametrów stawów dla płynniejszego sterowania
- Uproszczone geometrie kolizji dla szybszych obliczeń

## Dodatkowe zasoby

- [Oficjalna dokumentacja Unitree G1](https://support.unitree.com/home/en/G1_developer)
- [Specyfikacja techniczna G1](https://www.unitree.com/g1/)
- [Forum społeczności](https://discord.gg/ZwcVwxv5rq)
- [Przykłady użycia URDF](https://github.com/unitreerobotics/unitree_ros)

## Często zadawane pytania (FAQ)

**P: Jaka jest różnica między URDF a MJCF?**
O: URDF jest standardem ROS (Robot Operating System), MJCF jest formatem MuJoCo. Zawierają podobne informacje, ale MJCF ma więcej opcji dla symulacji fizycznej.

**P: Czy mogę używać tych plików w innych symulatorach?**
O: Tak! URDF działa z ROS, Gazebo, PyBullet. MJCF działa z MuJoCo i Isaac Sim (po konwersji).

**P: Jak zmodyfikować model pod swoje potrzeby?**
O: Edytuj pliki XML bezpośrednio, ale uważaj na składnię. Zalecamy skopiować oryginalny plik przed modyfikacją.

**P: Dlaczego niektóre wersje są oznaczone jako "Beta"?**
O: Te wersje mogą nie być w pełni przetestowane lub zoptymalizowane. Dla produkcji używaj wersji "Aktualne".
