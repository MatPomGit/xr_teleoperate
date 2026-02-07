# Contributing to xr_teleoperate

Thank you for your interest in contributing to xr_teleoperate! This document provides guidelines for contributing to the project.

[🇵🇱 Wersja polska](#współtworzenie-xr_teleoperate) | [English](#contributing-to-xr_teleoperate)

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the problem
- Expected behavior vs actual behavior
- Your environment (OS, Python version, hardware)
- Relevant logs or screenshots

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear description of the enhancement
- Rationale for why this would be useful
- Possible implementation approach (if you have ideas)

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Follow the development setup** guide in [DEVELOPMENT.md](DEVELOPMENT.md)
3. **Make your changes** following our coding standards
4. **Add tests** if applicable
5. **Update documentation** if needed
6. **Run the test suite** to ensure nothing breaks
7. **Submit a pull request** with a clear description

### Development Process

1. Clone the repository with submodules:
```bash
git clone --recursive https://github.com/MatPomGit/xr_teleoperate.git
cd xr_teleoperate
```

2. Install development dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development tools
pip install -e .  # Install in editable mode
```

3. Make your changes and test them:
```bash
# Run tests
pytest

# Check code style
flake8 teleop/

# Format code
black teleop/
isort teleop/
```

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Maximum line length: 100 characters
- Use type hints where appropriate
- Add docstrings to functions and classes
- Write comments in Polish or English

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Reference issue numbers when applicable (e.g., "Fix #123")
- Keep the first line under 72 characters

Example:
```
Add support for custom robot configurations

- Implement config file parser
- Add validation for robot parameters
- Update documentation

Fixes #123
```

### Testing

- Write tests for new features
- Ensure existing tests pass
- Aim for good test coverage
- Test on real hardware if possible

### Documentation

- Update README.md if adding new features
- Update CHANGELOG.md following the existing format
- Add docstrings to new functions and classes
- Update type hints
- Consider adding examples

## Code of Conduct

Please note that this project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## Questions?

Feel free to ask questions by:
- Creating an issue
- Joining our [Discord](https://discord.gg/ZwcVwxv5rq)
- Checking the [Wiki](https://github.com/unitreerobotics/xr_teleoperate/wiki)

---

# Współtworzenie xr_teleoperate

Dziękujemy za zainteresowanie współtworzeniem projektu xr_teleoperate! Ten dokument zawiera wytyczne dotyczące współpracy.

## Jak współtworzyć

### Zgłaszanie błędów

Jeśli znajdziesz błąd, utwórz issue zawierające:
- Jasny, opisowy tytuł
- Kroki do odtworzenia problemu
- Oczekiwane zachowanie vs rzeczywiste zachowanie
- Twoje środowisko (system operacyjny, wersja Python, sprzęt)
- Odpowiednie logi lub zrzuty ekranu

### Sugerowanie ulepszeń

Sugestie ulepszeń są mile widziane! Utwórz issue zawierające:
- Jasny opis ulepszenia
- Uzasadnienie, dlaczego byłoby to przydatne
- Możliwe podejście do implementacji (jeśli masz pomysły)

### Pull Requesty

1. **Zforkuj repozytorium** i utwórz swoją gałąź z `main`
2. **Postępuj zgodnie z przewodnikiem** w [DEVELOPMENT.md](DEVELOPMENT.md)
3. **Wprowadź zmiany** zgodnie z naszymi standardami kodowania
4. **Dodaj testy** jeśli to możliwe
5. **Zaktualizuj dokumentację** jeśli potrzeba
6. **Uruchom testy** aby upewnić się, że nic się nie zepsuło
7. **Wyślij pull request** z jasnym opisem

### Proces deweloperski

1. Sklonuj repozytorium z submodułami:
```bash
git clone --recursive https://github.com/MatPomGit/xr_teleoperate.git
cd xr_teleoperate
```

2. Zainstaluj zależności deweloperskie:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Narzędzia deweloperskie
pip install -e .  # Instalacja w trybie edytowalnym
```

3. Wprowadź zmiany i przetestuj je:
```bash
# Uruchom testy
pytest

# Sprawdź styl kodu
flake8 teleop/

# Formatuj kod
black teleop/
isort teleop/
```

### Styl kodu

- Przestrzegaj wytycznych PEP 8
- Używaj znaczących nazw zmiennych i funkcji
- Maksymalna długość linii: 100 znaków
- Używaj type hints tam gdzie to możliwe
- Dodawaj docstringi do funkcji i klas
- Pisz komentarze po polsku lub angielsku

### Komunikaty commit

- Używaj jasnych, opisowych komunikatów
- Zaczynaj od czasownika w czasie teraźniejszym (np. "Add", "Fix", "Update")
- Odwołuj się do numerów issues gdy to właściwe (np. "Fix #123")
- Pierwsza linia powinna mieć mniej niż 72 znaki

Przykład:
```
Add support for custom robot configurations

- Implement config file parser
- Add validation for robot parameters
- Update documentation

Fixes #123
```

### Testowanie

- Pisz testy dla nowych funkcji
- Upewnij się, że istniejące testy przechodzą
- Dąż do dobrego pokrycia testami
- Testuj na prawdziwym sprzęcie jeśli to możliwe

### Dokumentacja

- Aktualizuj README.md przy dodawaniu nowych funkcji
- Aktualizuj CHANGELOG.md zgodnie z istniejącym formatem
- Dodawaj docstringi do nowych funkcji i klas
- Aktualizuj type hints
- Rozważ dodanie przykładów

## Kodeks postępowania

Ten projekt przestrzega naszego [Kodeksu postępowania](CODE_OF_CONDUCT.md). Uczestnicząc, zobowiązujesz się do przestrzegania tego kodeksu.

## Pytania?

Możesz zadawać pytania poprzez:
- Tworzenie issue
- Dołączenie do naszego [Discorda](https://discord.gg/ZwcVwxv5rq)
- Sprawdzenie [Wiki](https://github.com/unitreerobotics/xr_teleoperate/wiki)
