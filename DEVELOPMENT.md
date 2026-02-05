# Development Setup Guide

## Installation

### 1. Clone the repository with submodules
```bash
git clone --recursive https://github.com/MatPomGit/xr_teleoperate.git
cd xr_teleoperate
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Install the package in development mode
```bash
pip install -e .
```

## Project Structure

```
xr_teleoperate/
├── teleop/              # Main package
│   ├── robot_control/   # Robot arm and hand controllers
│   ├── utils/           # Utility modules
│   └── teleop_hand_and_arm.py  # Main entry point
├── assets/              # Robot URDF models
├── tests/               # Test suite
├── setup.py             # Package configuration
├── requirements.txt     # Python dependencies
└── pytest.ini           # Test configuration
```

## Running Tests

```bash
pytest
```

## Code Quality

Check code style:
```bash
flake8 teleop/
```

Format code:
```bash
black teleop/
```

Sort imports:
```bash
isort teleop/
```
