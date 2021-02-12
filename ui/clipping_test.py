from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from ui.misc import StackedText
from ui.sliders import ClippingXSlider, ClippingYSlider, ClippingWidthSlider, ClippingHeightSlider


class ClippingTest(QWidget):

    def __init__(self, drawarea):
        super().__init__()
        self._main_layout = QVBoxLayout()
        self.setLayout(self._main_layout)
        self._label = QLabel("Тест отсечения")
        self._label_x = QLabel("X: ")
        self._label_y = QLabel("Y: ")
        self._label_width = QLabel("Width: ")
        self._label_height = QLabel("Height: ")
        self._label_x_level = QLabel("")
        self._label_y_level = QLabel("")
        self._label_width_level = QLabel("")
        self._label_height_level = QLabel("")
        self._x_slider = ClippingXSlider(drawarea, self._label_x_level)
        self._y_slider = ClippingYSlider(drawarea, self._label_y_level)
        self._width_slider = ClippingWidthSlider(drawarea, self._label_width_level)
        self._height_slider = ClippingHeightSlider(drawarea, self._label_height_level)
        self._main_layout.addWidget(self._label)
        self._main_layout.addWidget(StackedText(self._label_x, self._label_x_level))
        self._main_layout.addWidget(self._x_slider)
        self._main_layout.addWidget(StackedText(self._label_y, self._label_y_level))
        self._main_layout.addWidget(self._y_slider)
        self._main_layout.addWidget(StackedText(self._label_width, self._label_width_level))
        self._main_layout.addWidget(self._width_slider)
        self._main_layout.addWidget(StackedText(self._label_height, self._label_height_level))
        self._main_layout.addWidget(self._height_slider)
