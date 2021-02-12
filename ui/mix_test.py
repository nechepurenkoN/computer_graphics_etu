from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel

from ui.combos import SFactorCombo, DFactorCombo


class MixTest(QWidget):

    def __init__(self, drawarea):
        super().__init__()
        self._main_layout = QVBoxLayout()
        self.setLayout(self._main_layout)
        self._label = QLabel("Тест смешения")
        self._label_s = QLabel("sfactor")
        self._label_d = QLabel("dfactor")
        self._combo_s = SFactorCombo(drawarea)
        self._combo_d = DFactorCombo(drawarea)
        self._main_layout.addWidget(self._label)
        self._main_layout.addWidget(self._label_s)
        self._main_layout.addWidget(self._combo_s)
        self._main_layout.addWidget(self._label_d)
        self._main_layout.addWidget(self._combo_d)