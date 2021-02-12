from PyQt5.QtWidgets import QWidget, QHBoxLayout


class StackedText(QWidget):

    def __init__(self, *items):
        super().__init__()
        self._main_layout = QHBoxLayout()
        self.setLayout(self._main_layout)
        for item in items:
            self._main_layout.addWidget(item)
