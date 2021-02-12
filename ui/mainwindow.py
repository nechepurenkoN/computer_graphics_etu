from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import Qt

from ui.controlgroup import ControlGroup
from ui.drawarea import DrawArea


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMaximumSize(1000, 500)
        self.setMinimumSize(1000, 500)
        self.setWindowTitle("Лабораторная работа №1,2")
        self._main_widget = QtWidgets.QWidget()
        self._main_layout = QtWidgets.QHBoxLayout()
        self._draw_area = DrawArea()
        self._control_group_scroll = QScrollArea()
        self._control_group_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._control_group = ControlGroup(self._draw_area)
        self._set_layout()

    def _set_layout(self):
        self.setCentralWidget(self._main_widget)
        self._main_widget.setLayout(self._main_layout)
        self._main_layout.addWidget(self._draw_area)
        self._main_layout.addWidget(self._control_group_scroll)
        self._control_group_scroll.setWidget(self._control_group)
