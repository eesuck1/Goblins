import pygame


class Item:
    def __init__(self, weight: float, volume: float, icon: pygame.Surface, name: str):
        self._weight_ = weight
        self._volume_ = volume
        self._icon_ = icon
        self._name_ = name

    @property
    def name(self) -> str:
        return self._name_

    @property
    def icon(self) -> pygame.Surface:
        return self._icon_

    @property
    def volume(self) -> float:
        return self._volume_

    @property
    def weight(self) -> float:
        return self._weight_
