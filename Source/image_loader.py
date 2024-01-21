from typing import Any

from Source.body import Special
from Source.nature import Ground, Plant
from Source.constants import *

import os.path

import pygame


def open_image(root: str, file: str, collectable_root: str = "", collectable: str = "") -> pygame.Surface | tuple[
    pygame.Surface, pygame.Surface]:
    if collectable_root and collectable:
        return (pygame.image.load(os.path.join(root, file)),
                pygame.image.load(os.path.join(collectable_root, collectable)))

    return pygame.image.load(os.path.join(root, file))


def update_tile_map(root: str, kind: Any, collectable_root: str = "", *args, **kwargs) -> None:
    folder = os.listdir(root)
    collectable_folder = os.listdir(collectable_root) if collectable_root else None
    tile_map_length = len(TILE_MAP)

    updater = {}

    if collectable_folder:
        for index, (file, collectable) in zip(range(tile_map_length, tile_map_length + len(folder)),
                                              zip(folder, collectable_folder)):
            name = file.split(".")[0].split("_")[1]
            updater[index] = kind(*open_image(root, file, collectable_root, collectable), name=name, *args, **kwargs)
    else:
        for index, file in zip(range(tile_map_length, tile_map_length + len(folder)), folder):
            name = file.split(".")[0].split("_")[1]
            updater[index] = kind(open_image(root, file), name=name, *args, **kwargs)

    TILE_MAP.update(updater)


def load_images() -> None:
    update_tile_map(SPECIAL_TILES, Special)
    update_tile_map(GROUND_TILES, Ground)
    update_tile_map(COLLECTABLE_END, Plant, COLLECTABLE_START, can_collide=True)


def load_character(folder: str) -> tuple[pygame.Surface, ...]:
    return tuple([pygame.image.load(os.path.join(folder, file)) for file in os.listdir(folder)])
