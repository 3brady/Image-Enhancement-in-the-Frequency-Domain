# Image Enhancement in the Frequency Domain

A Python application for exploring frequency-domain and spatial image enhancement. The desktop interface uses PySide6 (Qt), and images are loaded and saved with OpenCV.

## Setup

Create a virtual environment in the project directory:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate       # Linux/macOS
# .venv\Scripts\activate      # Windows PowerShell
```

Install the project dependencies and start the GUI:

```bash
python -m pip install -r requirements.txt
python main.py
```

## Dependencies

`requirements.txt` lists the packages the project imports directly. To add a dependency, install it in the active virtual environment and add its package name to that file:

```bash
python -m pip install package-name
```

## Project files

- `main.py` starts the application.
- `gui.py` implements the Qt interface.
- `methods.py` lists the available filters.
- `frequency.py`, `lowpass.py`, `highpass.py`, `bandpass.py`, and `homomorphic.py` contain frequency-domain processing.
- `spatial.py` contains spatial-domain filters.
- `compare.py` compares paired frequency and spatial methods.
- `images/`, `results/`, and `report/` hold sample images, generated results, and project documentation.

Filters are expected to accept and return same-size grayscale `uint8` images.
