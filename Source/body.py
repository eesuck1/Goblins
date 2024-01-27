import random

import pygame


class Body:
    def __init__(self, image: pygame.Surface, name: str = f"BaseName_{random.random()}", can_collide: bool = False):
        self._image_ = image
        self._collide_ = can_collide
        self._name_ = name

        self._rect_ = pygame.rect.Rect(-2 ** 31, -2 ** 31, image.get_width(), image.get_height())

    @property
    def image(self) -> pygame.Surface:
        return self._image_

    @property
    def rect(self) -> pygame.Rect:
        return self._rect_

    @property
    def can_collide(self) -> bool:
        return self._collide_

    @can_collide.setter
    def can_collide(self, value: bool) -> None:
        self._collide_ = value

    @rect.setter
    def rect(self, value: tuple[int, int]):
        self._rect_.x = value[0]
        self._rect_.y = value[1]

    @property
    def name(self) -> str:
        return self._name_

    def __str__(self) -> str:
        return self._name_

    def __repr__(self) -> str:
        return self._name_


class Collectable(Body):
    def __init__(self, image: pygame.Surface, collected_image: pygame.Surface, name: str, can_collide: bool = True):
        super().__init__(image, name=name, can_collide=can_collide)

        self._collected_image_ = collected_image
        self._current_image_ = self._image_

        self._picked_ = False

    @property
    def image(self) -> pygame.Surface:
        return self._current_image_

    @property
    def picked(self) -> bool:
        return self._picked_

    def pick(self) -> None:
        self._current_image_ = self._collected_image_
        self._picked_ = True
        self._collide_ = False


class Special(Body):
    def __init__(self, image: pygame.Surface, name: str = f"Special_{random.random()}"):
        super().__init__(image, name=name)
