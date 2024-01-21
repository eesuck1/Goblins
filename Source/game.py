import random
import sys

import pygame

from Source.constants import *
from Source.map import Map
from Source.characters import Character, Player
from Source.image_loader import load_images, load_character
from Source.nature import Ground


class Game:
    def __init__(self):
        load_images()
        self._display_ = pygame.display.set_mode(WINDOW_SIZE)
        self._screen_ = pygame.Surface(DISPLAY_SIZE)
        self._clock_ = pygame.time.Clock()

        self._tile_map_ = Map().map
        print(self._tile_map_)

        self._player_ = self.init_player()

        self._characters_: list[Character, ...] = []
        self._objects_to_draw_ = {}

        self._current_level_ = 0

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    response = self._player_.actions(event, self.around_character(self._player_))

                    if response:
                        self.draw_text(response.message)

            self.draw_tiles()
            self.draw_characters()
            self.move_characters()
            self.draw_some_time()

            self._display_.blit(pygame.transform.scale(self._screen_, WINDOW_SIZE), (0, 0))
            self._clock_.tick(FPS)

            pygame.display.update()

    def draw_tiles(self) -> None:
        x, y, z = self._tile_map_.shape

        for i in range(x):
            for j in range(y):
                coordinates = (i * TILE_SIZE, j * TILE_SIZE)

                current_tile = self._tile_map_[i][j][self._current_level_]
                if not isinstance(current_tile, Ground):
                    current_tile.rect = coordinates

                self._screen_.blit(current_tile.image, coordinates)

    def draw_characters(self) -> None:
        for character in self._characters_ + [self._player_]:
            self._screen_.blit(character.image, character.coordinates)

    def move_characters(self) -> None:
        ...

    def draw_text(self, text: str) -> None:
        # TODO: create own text rendering process
        message = FONT.render(text, True, (230, 230, 230))
        message = pygame.transform.scale(message, (60, 15))

        self.add_to_some_time_queue(message, ((DISPLAY_SIZE[0] - message.get_width()) // 2, DISPLAY_SIZE[1] - 20), 60)

    def add_to_some_time_queue(self, object_to_draw: pygame.Surface, coordinates: tuple[int, int], frames: int) -> None:
        self._objects_to_draw_[(object_to_draw, coordinates)] = frames

    def draw_some_time(self) -> None:
        for form, frames in self._objects_to_draw_.items():
            if frames == 0:
                del self._objects_to_draw_[form]

                return

            self._screen_.blit(form[0], form[1])
            self._objects_to_draw_[form] -= 1

    def around_character(self, character: Character) -> list[pygame.rect.Rect, ...]:
        x, y = character.coordinates

        x //= TILE_SIZE
        y //= TILE_SIZE

        return [self._tile_map_[i][j][self._current_level_]
                for i, j in [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]]

    @staticmethod
    def load() -> None:
        load_images()

    @staticmethod
    def init_player() -> Player:
        player = Player(load_character(MAIN_CHARACTER_FOLDER), health=10, move_speed=1)

        x, y = DISPLAY_SIZE[0] // 8, DISPLAY_SIZE[1] // 8
        player.rect = random.randint(5, x - 5) * TILE_SIZE, random.randint(5, y - 5) * TILE_SIZE

        return player
