import logging

from OpenGL.GL import *


def alpha_test(fn):
    def fn_wrapper(self):
        glEnable(GL_ALPHA_TEST)
        fn(self)
        glDisable(GL_ALPHA_TEST)

    return fn_wrapper


def blend_test(fn):
    def fn_wrapper(self):
        glEnable(GL_BLEND)
        fn(self)
        glDisable(GL_BLEND)

    return fn_wrapper


def scissor_test(fn):
    def fn_wrapper(self):
        glEnable(GL_SCISSOR_TEST)
        fn(self)
        glDisable(GL_SCISSOR_TEST)

    return fn_wrapper


class Drawer:

    def __init__(self):
        self._points = []
        self._params = {
            "mode": GL_POINTS,
            "alpha_mode": GL_ALWAYS,
            "alpha_ref": 0.9,
            "s_factor": GL_ONE,
            "d_factor": GL_ZERO,
            "x_clip": 0,
            "y_clip": 0,
            "width_clip": 600,
            "height_clip": 480
        }

    def set_param(self, param_name, value):
        assert param_name in self._params
        self._params[param_name] = value

    def _set_color(self, color):
        glColor4f(*color)

    def _add_vertex(self, coords):
        glVertex2f(*coords)

    def handle_candidate(self, candidate_point):  # terrible, but works
        del_index = -1
        for idx, point in enumerate(self._points):
            if point == candidate_point:
                del_index = idx
                break
        if del_index + 1:
            logging.info(f"Deleting {self._points[del_index]}")
            del self._points[del_index]
        else:
            logging.info(f"Appending {candidate_point}")
            self._points.append(candidate_point)

    @scissor_test
    @blend_test
    @alpha_test
    def paint(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glScissor(self._params["x_clip"], self._params["y_clip"],
                  self._params["width_clip"], self._params["height_clip"])
        glAlphaFunc(self._params["alpha_mode"], self._params["alpha_ref"])
        glBlendFunc(self._params["s_factor"], self._params["d_factor"])
        glBegin(self._params["mode"])
        for point in self._points:
            self._set_color(point.color)
            self._add_vertex(point.get_coords())
        glEnd()
