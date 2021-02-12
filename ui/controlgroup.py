from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from ui.lab1 import Lab1
from ui.lab2 import Lab2


class ControlGroup(QWidget):

    def __init__(self, drawarea):
        super().__init__()
        self._drawarea = drawarea
        self._main_layout = QVBoxLayout()
        self.setLayout(self._main_layout)
        self._lab1_widget = Lab1(drawarea)
        self._main_layout.addWidget(self._lab1_widget)
        self._lab2_widget = Lab2(drawarea)
        self._main_layout.addWidget(self._lab2_widget)
        self._desc_label = QLabel("Для добавления точки нажмите на область рисования.\nЧтобы удалить точку, нажмите на неё.\nВыполнил ст. гр. 8382 Нечепуренко Н.А.")
        self._main_layout.addWidget(self._desc_label)
