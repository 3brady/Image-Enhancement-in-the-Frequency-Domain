import os

import cv2
import numpy as np

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
PREVIEW_SIZE = 400


def _pixmap(gray):
    gray = np.ascontiguousarray(gray)
    height, width = gray.shape
    image = QImage(gray.data, width, height, gray.strides[0], QImage.Format.Format_Grayscale8)
    return QPixmap.fromImage(image.copy()).scaled(
        PREVIEW_SIZE,
        PREVIEW_SIZE,
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation,
    )
