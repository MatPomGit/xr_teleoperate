# Przewodnik po Polskiej Dokumentacji - xr_teleoperate

## 🎓 Dla Studentów i Początkujących

Ten projekt został dostosowany pod kątem edukacyjny dla studentów i osób dopiero uczących się robotyki. Wszystkie opisy zostały przetłumaczone na język polski i znacznie rozbudowane.

## 📚 Dostępna Dokumentacja w Języku Polskim

### Główne Dokumenty

| Dokument | Opis | Dla Kogo |
|----------|------|----------|
| [README_pl.md](README_pl.md) | Kompletny przewodnik instalacji i użytkowania | **ZACZNIJ TUTAJ** - Wszyscy użytkownicy |
| [Device_pl.md](Device_pl.md) | Szczegółowy przewodnik sprzętowy | Osoby montujące sprzęt |
| [CHANGELOG_pl.md](CHANGELOG_pl.md) | Historia zmian projektu | Programiści śledzący rozwój |

### Dokumentacja Robotów

| Dokument | Opis |
|----------|------|
| [assets/g1/README_pl.md](assets/g1/README_pl.md) | Opis robota Unitree G1 (URDF/MJCF) |
| [assets/h1_2/README_pl.md](assets/h1_2/README_pl.md) | Opis robota Unitree H1 z 51 DoF |

## 🔍 Jak Korzystać z Tej Dokumentacji

### Jeśli Jesteś Początkującym:

1. **Przeczytaj najpierw [README_pl.md](README_pl.md)**
   - Rozdział 0: Zrozum czym jest teleoperation
   - Rozdział 1: Zainstaluj krok po kroku
   - Rozdział 2: Wypróbuj w symulacji (bezpieczne!)
   - Rozdział 3: Przejdź do fizycznego robota (gdy jesteś gotowy)

2. **Sprawdź [Device_pl.md](Device_pl.md) przed zakupem sprzętu**
   - Lista wymaganego sprzętu
   - Instrukcje montażu
   - FAQ dotyczące sprzętu

3. **Czytaj kod źródłowy z komentarzami**
   - Komentarze wyjaśniają "dlaczego" a nie tylko "co"
   - Terminy techniczne są wyjaśnione
   - Przykłady użycia

### Jeśli Jesteś Nauczycielem/Prowadzącym:

Zalecana kolejność materiałów dla zajęć:

**Lekcja 1: Wprowadzenie**
- Co to jest robot humanoidalny?
- Co to jest teleoperation?
- Demo wideo z README_pl.md

**Lekcja 2-3: Teoria**
- Stopnie swobody (DoF) - zobacz assets/h1_2/README_pl.md
- Kinematyka odwrotna (IK)
- Systemy współrzędnych

**Lekcja 4-5: Instalacja**
- Środowisko wirtualne (conda)
- Instalacja zależności
- Rozwiązywanie problemów

**Lekcja 6-8: Symulacja**
- Uruchomienie symulatora Isaac
- Pierwsze sterowanie w VR
- Nagrywanie danych

**Lekcja 9+: Projekt**
- Praca z fizycznym robotem
- Zbieranie własnych danych
- Eksperyment końcowy

## 💡 Kluczowe Pojęcia Wyjaśnione

### Dla Początkujących - Słowniczek:

- **Teleoperation (Teleoperation)** - Zdalne sterowanie robotem w czasie rzeczywistym
- **XR (Extended Reality)** - Ogólna nazwa dla VR/AR/MR
- **DoF (Degrees of Freedom)** - Stopnie swobody, liczba niezależnych ruchów
- **IK (Inverse Kinematics)** - Kinematyka odwrotna, obliczanie kątów stawów
- **End-effector** - Efektor końcowy, "dłoń" robota (chwytaki, dłonie zręcznościowe)
- **DDS (Data Distribution Service)** - Protokół komunikacji z robotem
- **URDF (Unified Robot Description Format)** - Format opisu robota w XML
- **Episode (Epizod)** - Jedna sesja nagrywania danych
- **Retargeting** - Mapowanie ruchów człowieka na robota

### Zaawansowane Terminy:

- **Imitation Learning** - Uczenie przez naśladowanie, robot uczy się z demonstracji
- **WebRTC** - Protokół do transmisji wideo w czasie rzeczywistym
- **Pinocchio** - Biblioteka do obliczeń kinematyki
- **MuJoCo** - Symulator fizyki dla robotyki
- **ROS** - Robot Operating System, framework dla robotów

## 🎯 Cele Edukacyjne

Po przejściu przez tę dokumentację i kod, powinieneś umieć:

### Poziom Podstawowy:
- ✅ Zrozumieć czym jest teleoperation
- ✅ Zainstalować i uruchomić symulację
- ✅ Sterować robotem w symulacji
- ✅ Zrozumieć podstawową strukturę projektu

### Poziom Średnio-Zaawansowany:
- ✅ Pracować z fizycznym robotem
- ✅ Nagrywać dane treningowe
- ✅ Czytać i rozumieć kod źródłowy
- ✅ Modyfikować parametry sterowania

### Poziom Zaawansowany:
- ✅ Modyfikować algorytmy kinematyki
- ✅ Dodawać własne funkcje
- ✅ Optymalizować wydajność
- ✅ Integrować z własnymi projektami ML

## 🤝 Wsparcie i Pomoc

### Gdzie Szukać Pomocy:

1. **FAQ w Dokumentacji**
   - Każdy dokument ma sekcję "Często zadawane pytania"
   - Sprawdź tam najpierw!

2. **Wiki Projektu**
   - [GitHub Wiki](https://github.com/unitreerobotics/xr_teleoperate/wiki)
   - Więcej szczegółowych przewodników

3. **Społeczność**
   - [Discord](https://discord.gg/ZwcVwxv5rq) - Czat na żywo
   - [GitHub Issues](https://github.com/unitreerobotics/xr_teleoperate/issues) - Zgłaszanie problemów

4. **Oficjalna Dokumentacja Unitree**
   - [Support Portal](https://support.unitree.com/)
   - Dokumentacja techniczna robotów

## 📊 Struktura Projektu - Szybki Przegląd

```
xr_teleoperate/
├── README_pl.md              ← ZACZNIJ TUTAJ!
├── Device_pl.md              ← Sprzęt i montaż
├── CHANGELOG_pl.md           ← Historia zmian
│
├── assets/                   ← Modele robotów (URDF/MJCF)
│   ├── g1/README_pl.md       ← Opis robota G1
│   └── h1_2/README_pl.md     ← Opis robota H1
│
└── teleop/                   ← Kod programu
    ├── teleop_hand_and_arm.py    ← Główny plik uruchomieniowy
    ├── robot_control/            ← Sterowanie robotem
    ├── utils/                    ← Narzędzia pomocnicze
    ├── teleimager/               ← Obsługa kamer
    └── televuer/                 ← Interfejs XR
```

## 🚀 Szybki Start dla Niecierpliwych

Jeśli chcesz jak najszybciej zacząć:

```bash
# 1. Utwórz środowisko
conda create -n tv python=3.10 pinocchio=3.1.0 numpy=1.26.4 -c conda-forge
conda activate tv

# 2. Sklonuj projekt
git clone https://github.com/unitreerobotics/xr_teleoperate.git
cd xr_teleoperate
git submodule update --init --depth 1

# 3. Zainstaluj zależności
cd teleop/teleimager && pip install -e . --no-deps && cd ../..
cd teleop/televuer && pip install -e . && cd ../..
cd .. && git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
cd unitree_sdk2_python && pip install -e . && cd ..

# 4. Uruchom symulację (wymaga Isaac Lab)
# Zobacz README_pl.md rozdział 2 dla szczegółów

# 5. Uruchom teleoperation
cd xr_teleoperate/teleop
python teleop_hand_and_arm.py --sim --ee=dex3
```

**UWAGA:** To tylko szybki przegląd! Przeczytaj pełną dokumentację dla bezpiecznej i poprawnej instalacji.

## 📖 Dodatkowe Zasoby

### Materiały do Nauki:

- **Robotyka Podstawy:**
  - [Kurs MIT OpenCourseWare](https://ocw.mit.edu/courses/mechanical-engineering/)
  - [Robot Academy](https://robotacademy.net.au/)

- **Python dla Robotyki:**
  - [Real Python Tutorials](https://realpython.com/)
  - [Python Robotics](https://github.com/AtsushiSakai/PythonRobotics)

- **ROS i Robotyka:**
  - [ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)
  - [Modern Robotics Textbook](http://hades.mech.northwestern.edu/index.php/Modern_Robotics)

### Projekty Podobne:

- [OpenTeleVision](https://github.com/OpenTeleVision/TeleVision)
- [Dex-Retargeting](https://github.com/dexsuite/dex-retargeting)
- [ARCLab beavr-bot](https://github.com/ARCLab-MIT/beavr-bot)

## 🎓 Dla Nauczycieli - Materiały Dydaktyczne

### Sugerowane Ćwiczenia:

**Ćwiczenie 1: Analiza Kinematyki**
- Zadanie: Zmierz rzeczywiste DoF robota i porównaj z modelem URDF
- Cel: Zrozumienie struktury kinematycznej

**Ćwiczenie 2: Kalibracja**
- Zadanie: Wykalib calibrate offsety stawów
- Cel: Praktyka pracy z fizycznym sprzętem

**Ćwiczenie 3: Zbieranie Danych**
- Zadanie: Nagraj 10 epizodów podnoszenia obiektu
- Cel: Zrozumienie procesu zbierania danych dla ML

**Ćwiczenie 4: Optymalizacja**
- Zadanie: Popraw częstotliwość sterowania z 30Hz do 50Hz
- Cel: Zrozumienie wydajności systemu

### Tematy Projektów:

1. Rozszerzenie o nowy typ chwytaka
2. Implementacja własnego algorytmu filtrowania
3. Analiza jakości danych nagranych
4. Wizualizacja trajektorii robota
5. Integracja z systemem wizji komputerowej

## ❓ Najczęściej Zadawane Pytania (Ogólne)

**P: Czy muszę mieć robota żeby zacząć?**
O: Nie! Możesz zacząć od symulacji. Zobacz rozdział 2 w README_pl.md.

**P: Jakie mam opcje jeśli nie mam gogli VR?**
O: Niestety gogle VR/AR są wymagane. Najtańsza opcja to Meta Quest 3S (~$300).

**P: Czy mogę użyć innego robota niż Unitree?**
O: Teoretycznie tak, ale wymaga to znaczących modyfikacji kodu. Projekt jest zoptymalizowany dla robotów Unitree.

**P: Jak długo trwa nauka całego systemu?**
O: Dla osoby z podstawami programowania i robotyki: ~2-4 tygodnie do biegłości podstawowej, ~2-3 miesiące do zaawansowanej.

**P: Czy mogę używać tego projektu komercyjnie?**
O: Zobacz plik LICENSE. Większość komponentów jest open-source, ale sprawdź licencje poszczególnych bibliotek.

## 📞 Kontakt

- **Issues:** [GitHub Issues](https://github.com/unitreerobotics/xr_teleoperate/issues)
- **Discord:** [Discord Server](https://discord.gg/ZwcVwxv5rq)
- **Email:** Sprawdź oficjalną stronę Unitree

---

**Ostatnia aktualizacja:** 2026-02-05
**Wersja dokumentacji:** 1.0
**Język:** Polski 🇵🇱

**Życzymy powodzenia w nauce robotyki! 🤖✨**
