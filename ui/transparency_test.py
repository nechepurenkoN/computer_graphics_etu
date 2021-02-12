from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from ui.combos import TransparencyCombo
from ui.misc import StackedText
from ui.sliders import AlphaRefSlider


class TransparencyTest(QWidget):

    def __init__(self, drawarea):
        super().__init__()
        self._main_layout = QVBoxLayout()
        self.setLayout(self._main_layout)
        self._label = QLabel("Тест прозрачности")
        self._label_mode = QLabel("Режим: ")
        self._label_threshold = QLabel("Пороговый уровень: ")
        self._label_threshold_level = QLabel("")
        self._mode = TransparencyCombo(drawarea)
        self._ref_slider = AlphaRefSlider(drawarea, self._label_threshold_level)
        self._main_layout.addWidget(self._label)
        self._main_layout.addWidget(self._label_mode)
        self._main_layout.addWidget(self._mode)
        self._main_layout.addWidget(StackedText(self._label_threshold, self._label_threshold_level))
        self._main_layout.addWidget(self._ref_slider)



