import random
import time
from copy import copy

import numpy
import pygame.event

from Source.constants import *


class Map:
    def __init__(self, initial_coordinates: numpy.ndarray):
        self._tile_map_ = TILE_MAP

        self._width_, self._height_ = DISPLAY_SIZE[0] // (2 * TILE_SIZE), DISPLAY_SIZE[1] // (2 * TILE_SIZE)
        self._map_ = numpy.full((MAX_WIDTH, MAX_HEIGHT, 8), TILE_MAP.get(1))

        self._current_x_, self._current_y_ = initial_coordinates
        self._current_level_ = 0

        self.generate_map(0, 0, self._current_level_)

    def map(self, coordinates: numpy.ndarray, current_level: int) -> numpy.ndarray:
        self._current_x_, self._current_y_ = coordinates

        center_x = MAX_WIDTH // 2 + self._current_x_
        center_y = MAX_HEIGHT // 2 + self._current_y_
        self._current_level_ = current_level

        return self._map_[center_x - self._width_:center_x + self._width_ + 1,
               center_y - self._height_:center_y + self._height_ + 1,
               current_level]

    def generate_map(self, x: int, y: int, current_level: int, seed: int = 0) -> None:
        random.seed(time.time()) if not seed else random.seed(seed)

        for _ in range(MAX_WIDTH * MAX_HEIGHT // 10):
            tile = copy(TILE_MAP.get(random.randint(2, len(TILE_MAP) - 1)))

            random_x = numpy.random.randint(0, MAX_HEIGHT - 1)
            random_y = numpy.random.randint(0, MAX_HEIGHT - 1)

            self._map_[random_x, random_y, current_level] = tile

    def __str__(self) -> str:
        return str(self._map_)
