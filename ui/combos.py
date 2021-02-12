from PyQt5.QtWidgets import QComboBox
from OpenGL.GL import *


class LabCombo(QComboBox):

    def __init__(self, drawarea):
        super().__init__()
        self._drawarea = drawarea
        self._initialize_items()
        for item in self._items:
            self.addItem(str(item).split()[0], item)
        self.currentTextChanged.connect(self.handler)

    def _initialize_items(self):
        self._items = []

    def handler(self):
        self._send_parameters()
        self._drawarea.updateGL()

    def _send_parameters(self):
        pass


class ModeCombo(LabCombo):

    def __init__(self, drawarea):
        super().__init__(drawarea)

    def _initialize_items(self):
        self._items = [GL_POINTS, GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP, GL_TRIANGLES, GL_TRIANGLE_STRIP,
                       GL_TRIANGLE_FAN, GL_QUADS, GL_QUAD_STRIP, GL_POLYGON]

    def _send_parameters(self):
        self._drawarea.get_drawer().set_param("mode", self.currentData())


class TransparencyCombo(LabCombo):

    def __init__(self, drawarea):
        super().__init__(drawarea)

    def _initialize_items(self):
        self._items = [GL_ALWAYS, GL_NEVER, GL_LESS, GL_EQUAL, GL_LEQUAL, GL_GREATER, GL_NOTEQUAL, GL_GEQUAL]

    def _send_parameters(self):
        self._drawarea.get_drawer().set_param("alpha_mode", self.currentData())


class SFactorCombo(LabCombo):

    def __init__(self, drawarea):
        super().__init__(drawarea)

    def _initialize_items(self):
        self._items = [GL_ONE, GL_ZERO, GL_DST_COLOR, GL_ONE_MINUS_DST_COLOR, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA,
                       GL_DST_ALPHA, GL_ONE_MINUS_DST_ALPHA, GL_SRC_ALPHA_SATURATE]

    def _send_parameters(self):
        self._drawarea.get_drawer().set_param("s_factor", self.currentData())


class DFactorCombo(LabCombo):

    def __init__(self, drawarea):
        super().__init__(drawarea)

    def _initialize_items(self):
        self._items = [GL_ZERO, GL_ONE, GL_SRC_COLOR, GL_ONE_MINUS_SRC_COLOR, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA,
                       GL_DST_ALPHA, GL_ONE_MINUS_DST_ALPHA]

    def _send_parameters(self):
        self._drawarea.get_drawer().set_param("d_factor", self.currentData())
