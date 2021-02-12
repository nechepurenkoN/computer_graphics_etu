from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from ui.combos import ModeCombo


class Lab1(QWidget):

    def __init__(self, drawarea):
        super().__init__()
        self._lab1_label = QLabel("Лабораторная работа №1")
        self._mode_select = ModeCombo(drawarea)
        self._main_layout = QVBoxLayout()
        self.setLayout(self._main_layout)
        self._main_layout.addWidget(self._lab1_label)
        self._main_layout.addWidget(self._mode_select)
