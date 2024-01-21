import random
import time

from copy import copy

from Source.constants import *
from Source.array import Array
from Source.image_loader import load_images


class Map:
    def __init__(self):
        self._tile_map_ = TILE_MAP

        self._x_, self._y_ = DISPLAY_SIZE[0] // TILE_SIZE, DISPLAY_SIZE[1] // TILE_SIZE
        self._map_ = Array((self._x_, self._y_, 1), TILE_MAP.get(1))

        self.generate_map()

    @property
    def map(self) -> Array:
        return self._map_

    def generate_map(self, seed: int = 0) -> None:
        if not seed:
            random.seed(time.time())

        for _ in range(self._x_ * self._y_ // 20):
            tile = copy(TILE_MAP.get(random.randint(2, len(TILE_MAP) - 1)))

            self._map_[random.randint(0, self._x_ - 1)][random.randint(0, self._y_ - 1)][0] = tile

    def __str__(self) -> str:
        return str(self._map_)
