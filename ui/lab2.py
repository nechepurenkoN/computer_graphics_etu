from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from ui.clipping_test import ClippingTest
from ui.mix_test import MixTest
from ui.transparency_test import TransparencyTest


class Lab2(QWidget):

    def __init__(self, drawarea):
        super().__init__()
        self._main_layout = QVBoxLayout()
        self.setLayout(self._main_layout)
        self._lab2_label = QLabel("Лабораторная работа №2")
        self._transparency = TransparencyTest(drawarea)
        self._mix = MixTest(drawarea)
        self._clipping = ClippingTest(drawarea)
        self._main_layout.addWidget(self._lab2_label)
        self._main_layout.addWidget(self._transparency)
        self._main_layout.addWidget(self._mix)
        self._main_layout.addWidget(self._clipping)
