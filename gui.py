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
class ImageEnhancementWindow(QMainWindow):
    def __init__(self, methods):
        super().__init__()
        self.methods = methods
        self.gray = None
        self.result = None
        self.image_path = None

        self.setWindowTitle("Image Enhancement in the Frequency Domain")

        self.method_choice = QComboBox()
        self.method_choice.addItems(methods.keys())
        self.method_choice.setEnabled(bool(methods))
        self.method_choice.currentTextChanged.connect(self.apply_filter)

        load_button = QPushButton("Load image")
        load_button.clicked.connect(self.load_image)
        self.save_button = QPushButton("Save result")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_result)

        controls = QHBoxLayout()
        controls.addWidget(load_button)
        controls.addWidget(self.method_choice)
        controls.addWidget(self.save_button)

        self.original_preview = QLabel("Original")
        self.result_preview = QLabel("Result")
        for preview in (self.original_preview, self.result_preview):
            preview.setFixedSize(PREVIEW_SIZE, PREVIEW_SIZE)
            preview.setScaledContents(False)
            preview.setStyleSheet("QLabel { background: #222; color: white; }")

        previews = QHBoxLayout()
        previews.addLayout(self._preview_column("Original", self.original_preview))
        previews.addLayout(self._preview_column("Result", self.result_preview))

        self.status = QLabel("Load an image to start.")
        layout = QVBoxLayout()
        layout.addLayout(controls)
        layout.addLayout(previews)
        layout.addWidget(self.status)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    @staticmethod
    def _preview_column(title, preview):
        column = QVBoxLayout()
        caption = QLabel(title)
        caption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column.addWidget(caption)
        column.addWidget(preview)
        return column

    def _show_image(self, label, gray):
        label.setPixmap(_pixmap(gray))
        label.setText("")

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Choose an image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.tif *.tiff);;All files (*)",
        )
        if not path:
            return

        gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if gray is None:
            QMessageBox.critical(self, "Image error", "Could not read this image.")
            return

        self.gray = gray
        self.image_path = path
        self.result = None
        self._show_image(self.original_preview, gray)
        self.result_preview.clear()
        self.result_preview.setText("Result")
        self.save_button.setEnabled(False)
        self.status.setText(f"Loaded: {os.path.basename(path)}")
        self.apply_filter()

    def apply_filter(self, *_):
        if self.gray is None or not self.methods:
            return

        name = self.method_choice.currentText()
        self.result = None
        self.save_button.setEnabled(False)
        try:
            result = self.methods[name](self.gray)
            if (
                not hasattr(result, "dtype")
                or str(result.dtype) != "uint8"
                or result.ndim != 2
                or result.shape != self.gray.shape
            ):
                raise ValueError("filter must return a same-size grayscale uint8 image")
        except Exception as error:
            self.result_preview.clear()
            self.result_preview.setText("Result")
            self.status.setText(f"{name} failed: {error}")
            QMessageBox.critical(self, "Filter error", f"{name} failed:\n{error}")
            return

        self.result = result
        self._show_image(self.result_preview, result)
        self.save_button.setEnabled(True)
        self.status.setText(f"Applied: {name}")

    def save_result(self):
        if self.result is None or self.image_path is None:
            return

        os.makedirs(RESULTS_DIR, exist_ok=True)
        base = os.path.splitext(os.path.basename(self.image_path))[0]
        name = self.method_choice.currentText().replace(" ", "_")
        output_path = os.path.join(RESULTS_DIR, f"{base}_{name}.png")
        if not cv2.imwrite(output_path, self.result):
            QMessageBox.critical(self, "Save error", "Could not save the result image.")
            return
        self.status.setText(f"Saved: {output_path}")


def run_app(methods):
    app = QApplication.instance() or QApplication([])
    window = ImageEnhancementWindow(methods)
    window.show()
    return app.exec()
