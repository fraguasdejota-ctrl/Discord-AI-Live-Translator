import sys

# --- 1. DECLARACIÓN EXPLÍCITA PARA PYINSTALLER ---
# Al estar traductor_core.pyd cifrado en C, declaramos aquí los módulos 
# externos para obligar a PyInstaller a empaquetarlos dentro del .exe:
import PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QLineEdit, QSystemTrayIcon, QMenu
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer, QPoint, QSettings
from PyQt6.QtGui import QIcon, QFont, QColor, QAction, QCursor
import numpy
import requests
import json
import threading
import queue
import time
import os

# Si usas pyaudiowpatch, soundcard, groq o faster_whisper en tu script original, 
# descomenta o deja los que realmente uses en tu código:
try:
    import pyaudiowpatch as pyaudio
except ImportError:
    pass
try:
    import faster_whisper
except ImportError:
    pass
try:
    import groq
except ImportError:
    pass

# --- 2. ARRANQUE DEL BINARIO PROTEGIDO EN C ---
import traductor_core

if __name__ == "__main__":
    traductor_core.iniciar_app()