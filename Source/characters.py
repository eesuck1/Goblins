import numpy
import pygame

from Source.body import Body, Collectable
from Source.constants import TILE_SIZE
from Source.inventory import Inventory, Item
from Source.message import ToSay, Refuse, Message


class Character(Body):
    def __init__(self, images: tuple[pygame.Surface, ...] | numpy.ndarray, health: int, move_speed: int):
        super().__init__(images[0])

        self._images_ = images
        self._image_pointer_ = 0

        self._health_ = health
        self._move_speed_ = move_speed

    @property
    def image(self) -> pygame.Surface:
        return self._images_[self._image_pointer_]

    @property
    def coordinates(self) -> numpy.ndarray:
        return numpy.array([self._rect_.x, self._rect_.y])

    def actions(self, event: pygame.event.Event, around: list[pygame.rect.Rect, ...]) -> None:
        ...


class Player(Character):
    def __init__(self, images: numpy.ndarray, health: int, move_speed: int):
        super().__init__(images, health, move_speed)

        self._inventory_ = Inventory()

    def actions(self, event: pygame.event.Event, around: numpy.ndarray) -> None | Message:
        right_tile, top_tile, left_tile, down_tile = around

        if event.key == pygame.K_a:
            self._image_pointer_ = 2

            if not left_tile.can_collide:
                self._rect_.x -= self._move_speed_

        elif event.key == pygame.K_d:
            self._image_pointer_ = 0

            if not right_tile.can_collide:
                self._rect_.x += self._move_speed_

        elif event.key == pygame.K_w:
            self._image_pointer_ = 1

            if not top_tile.can_collide:
                self._rect_.y -= self._move_speed_

        elif event.key == pygame.K_s:
            self._image_pointer_ = 3

            if not down_tile.can_collide:
                self._rect_.y += self._move_speed_

        if event.key == pygame.K_f:
            item = around[self._image_pointer_]

            if isinstance(item, Collectable) and not item.picked:
                response = self._inventory_.add_item(Item(15, 3, item.image, item.name))

                if isinstance(response, Refuse):
                    return response
                elif isinstance(response, ToSay):
                    item.pick()

                    return response
                else:
                    item.pick()
