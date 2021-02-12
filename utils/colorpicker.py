import itertools
import random

colors = list(itertools.combinations([1., 0., 0.7, 0.5, 0.3], 3))


class ColorPicker:

    @staticmethod
    def get_random_color():
        return [*random.choice(colors), random.random()]
