from OpenGL.GL import *
from PyQt5 import QtGui
from PyQt5.QtOpenGL import *

from utils.drawer import Drawer
from utils.point import Point2D


class DrawArea(QGLWidget):

    def __init__(self):
        self._drawer = Drawer()
        super().__init__()
        self.setMinimumSize(600, 480)
        self.resize(600, 480)

    def paintGL(self):
        self._drawer.paint()

    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(25, 25, 25))
        glLineWidth(1)
        self.qglColor(QtGui.QColor(255, 0, 0))

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def get_drawer(self):
        return self._drawer

    def mousePressEvent(self, event):
        candidate_point = Point2D((2*event.x()-self.width())/self.width(), (2*(self.height() - event.y())-self.height())/self.height())
        self._drawer.handle_candidate(candidate_point)
        self.updateGL()

