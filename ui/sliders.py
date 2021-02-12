from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt


class LabSlider(QSlider):

    def __init__(self, drawarea, level, normalized=True):
        super().__init__(Qt.Horizontal)
        self._drawarea = drawarea
        self._level = level
        self._normalized = normalized
        self._initialize_variables()
        self._initialize_state()
        self.valueChanged.connect(self._handler)

    def _initialize_variables(self):
        self._min = 0
        self._max = 100
        self._initial = 0

    def _initialize_state(self):
        self.setMinimum(self._min)
        self.setMaximum(self._max)
        self.setValue(self._initial)
        value_to_be_set = self.value()
        if self._normalized:
            value_to_be_set = self._normalize(value_to_be_set)
        self._level.setText(str(value_to_be_set))

    def _handler(self):
        value_to_be_set = self.value()
        if self._normalized:
            value_to_be_set = self._normalize(value_to_be_set)
        self._level.setText(str(value_to_be_set))
        self._send_parameters()
        self._drawarea.updateGL()

    def _send_parameters(self):
        pass

    def _normalize(self, value):
        return value / self._max


class AlphaRefSlider(LabSlider):

    def __init__(self, drawarea, level):
        super().__init__(drawarea, level)

    def _initialize_variables(self):
        self._min = 0
        self._max = 100
        self._initial = 90

    def _send_parameters(self):
        value_to_be_set = self._normalize(self.value())
        self._drawarea.get_drawer().set_param("alpha_ref", value_to_be_set)


class ClippingXSlider(LabSlider):

    def __init__(self, drawarea, level):
        super().__init__(drawarea, level, False)

    def _initialize_variables(self):
        self._min = 0
        self._max = 600
        self._initial = 0

    def _send_parameters(self):
        value_to_be_set = self.value()
        self._drawarea.get_drawer().set_param("x_clip", value_to_be_set)


class ClippingYSlider(LabSlider):

    def __init__(self, drawarea, level):
        super().__init__(drawarea, level, False)

    def _initialize_variables(self):
        self._min = 0
        self._max = 480
        self._initial = 0

    def _send_parameters(self):
        value_to_be_set = self.value()
        self._drawarea.get_drawer().set_param("y_clip", value_to_be_set)


class ClippingWidthSlider(LabSlider):

    def __init__(self, drawarea, level):
        super().__init__(drawarea, level, False)

    def _initialize_variables(self):
        self._min = 0
        self._max = 600
        self._initial = 600

    def _send_parameters(self):
        value_to_be_set = self.value()
        self._drawarea.get_drawer().set_param("width_clip", value_to_be_set)


class ClippingHeightSlider(LabSlider):

    def __init__(self, drawarea, level):
        super().__init__(drawarea, level, False)

    def _initialize_variables(self):
        self._min = 0
        self._max = 480
        self._initial = 480

    def _send_parameters(self):
        value_to_be_set = self.value()
        self._drawarea.get_drawer().set_param("height_clip", value_to_be_set)
