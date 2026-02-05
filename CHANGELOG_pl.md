# 🔖 Informacje o wydaniach

## 🏷️ v1.5 (2025.12.29)

- Wsparcie trybu symulacji
- Dodanie parametru nazwy interfejsu dla CycloneDDS
- Aktualizacja wersji teleimager
- [Migracja IPC do adresu wirtualnego @](https://github.com/unitreerobotics/xr_teleoperate/commit/46603c5ff385da7a9de59fb4a4a5dca1de4d9133)
- [Dodanie cache'owania aby przyspieszyć wczytywanie URDF](https://github.com/unitreerobotics/xr_teleoperate/commit/6cab654620735bfa347c1cd32a0d8c0c1e6ec343)

## 🏷️ v1.4 (2025.11.21)

- **Serwer obrazu** został zmieniony na [teleimager](https://github.com/silencht/teleimager). Szczegóły w README repozytorium.

- [televuer](https://github.com/silencht/televuer) zostało zaktualizowane. Szczegóły w README repozytorium.

  > Nowe wersje [teleimager](https://github.com/silencht/teleimager/commit/ab5018691943433c24af4c9a7f3ea0c9a6fbaf3c) + [televuer](https://github.com/silencht/televuer/releases/tag/v3.0) obsługują transmisję obrazów z kamery głowy przez **WebRTC**.

- Wzbogacone parametry informacji o zadaniu w **trybie nagrywania**, naprawienie i ulepszenie EpisodeWriter.
- Ulepszona informacja o **maszynie stanów** systemu i trybie IPC.
- Dodanie **trybu pass-through**, umożliwiającego bezpośrednie oglądanie zewnętrznego środowiska przez kamerę urządzenia VR (bez używania kamery głowy robota).
- Dodanie **trybu powinowactwa CPU**. Jeśli nie znasz tego trybu, możesz go zignorować.
- Dodanie funkcjonalności **motion-switcher**, umożliwiającej automatyczne wejście i wyjście z trybu debug bez użycia pilota zdalnego sterowania.

## 🏷️ v1.3 (2025.10.14)

- Dodanie [![Unitree LOGO](https://camo.githubusercontent.com/ff307b29fe96a9b115434a450bb921c2a17d4aa108460008a88c58a67d68df4e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d57696b692d3138313731373f6c6f676f3d676974687562)](https://github.com/unitreerobotics/xr_teleoperate/wiki) [![Unitree LOGO](https://camo.githubusercontent.com/6f5253a8776090a1f89fa7815e7543488a9ec200d153827b4bc7c3cb5e1c1555/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d446973636f72642d3538363546323f7374796c653d666c6174266c6f676f3d446973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.gg/ZwcVwxv5rq)

- Wsparcie **trybu IPC**, domyślnie używa SSHKeyboard do sterowania wejściem.
- Połączenie wsparcia trybu ruchu dla robota H1_2.
- Połączenie wsparcia trybu ruchu dla ramienia robota G1_23.

------

- Optymalizacja funkcjonalności nagrywania danych.
- Ulepszone użycie chwytaka w środowisku symulacyjnym.

------

- Naprawiono oscylacje przy starcie przez inicjalizację IK przed aktywacją kontrolera.
- Naprawiono błąd zatrzymywania nasłuchiwania SSHKeyboard.
- Naprawiono logikę przycisku start.
- Naprawiono różne błędy w trybie symulacji.

## 🏷️ v1.2 (2025.7.22)

- Wsparcie dla dłoni zręcznościowej BrainCo.
- Wsparcie dla chwytaka Dex1-1.
- Obsługa zapisywania danych treningowych z urządzenia XR do pliku.
- Zaimplementowano filtr wygładzający dla pozycji stawów ramienia.
- Dodano parametry `--task-*` do opisywania informacji o zadaniu w trybie nagrywania.
- Dodano możliwość ręcznego zatrzymywania nagrywania.

------

- Usunięto zależności od meshcat i uruchomiliśmy meshcat w tle.
- Usunięto zależności od teleimager, teraz [teleimager](https://github.com/silencht/teleimager) jest submodułem.

------

- Naprawiono błąd polegający na tym, że pętla nagrywania głównej nici nie mogła opuścić pierwszego nagrania przy użyciu try-finally.
- Naprawiono błąd w argumencie `--frequency` dla EpisodeWriter.

## 🏷️ v1.1 (2025.7.1)

**WAŻNE:** Ta wersja wymaga aktualizacji `unitree_sdk2_python`. Zobacz instrukcje instalacji.

- Wsparcie dla trybu Motion Control (tryb ruchu).
- Wsparcie dla kontrolera jako urządzenia śledzenia wejścia XR.
- Wsparcie dla dłoni zręcznościowej Inspire (tylko FTP, DFX w przyszłości).
- Wsparcie dla kamery D405 zamontowanej na nadgarstku.
- Dodano wideo demonstracyjne H1_2 (ramię 7-DoF).

------

- Połączono gałąź h1_2.
- Zaktualizowano diagr schemat połączeń urządzeń.

------

- Naprawiono błędy ortograficzne.

## 🏷️ v1.0 (2025.6.14)

- **Pierwsze publiczne wydanie! 🎉**
- Wsparcie dla robota G1 (29-DoF i 23-DoF).
- Wsparcie dla robota H1 (ramię 4-DoF).
- Wsparcie dla dłoni zręcznościowej Dex3-1.
- Wsparcie dla urządzeń XR: Apple Vision Pro, PICO 4 Ultra Enterprise, Meta Quest 3.
- Podstawowe funkcje teleoperation.
- Dokumentacja w języku angielskim i chińskim.

---

## 📝 O tym pliku

Ten plik dokumentuje wszystkie istotne zmiany w projekcie xr_teleoperate.

Format bazuje na [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
a projekt stosuje [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### Typy zmian

- **Dodanie** - dla nowych funkcji
- **Zmiana** - dla zmian w istniejących funkcjach
- **Dezaprobowane** - dla funkcji, które wkrótce zostaną usunięte
- **Usunięte** - dla usuniętych funkcji
- **Naprawione** - dla poprawek błędów
- **Bezpieczeństwo** - w przypadku luk w zabezpieczeniach
