import pygame

from Source.body import Collectable, Body


class Ground(Body):
    def __init__(self, image: pygame.Surface, name: str, can_collide: bool = False):
        super().__init__(image, name, can_collide)


class Plant(Collectable):
    def __init__(self, image: pygame.Surface, collected_image: pygame.Surface, name: str, can_collide: bool = False):
        super().__init__(image, collected_image, name, can_collide=can_collide)
