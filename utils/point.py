import hashlib
import math

from utils.colorpicker import ColorPicker

sha = hashlib.sha256()


class Point2D:
    def __init__(self, x=0., y=0.):
        self.x = x
        self.y = y
        sha.update(f"{self.x}_{self.y}".encode())
        self.id = sha.hexdigest()
        self.color = ColorPicker.get_random_color()

    def get_coords(self):
        return [self.x, self.y]

    def __str__(self):
        return f"Point2D[{self.x}, {self.y}] {self.id}"

    def __eq__(self, other):
        assert isinstance(other, Point2D)
        return math.dist([*self.get_coords()], [*other.get_coords()]) < 2e-2

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return self.__str__()