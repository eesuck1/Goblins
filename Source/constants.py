import pygame.font
pygame.init()

WINDOW_SIZE = (1280, 720)
DISPLAY_SIZE = (240, 136)
TILE_SIZE = 8

GROUND_TILES = "Assets/Tiles/Ground"
SPECIAL_TILES = "Assets/Tiles/Special"
COLLECTABLE_START = "Assets/Tiles/Collectable/Collected"
COLLECTABLE_END = "Assets/Tiles/Collectable/Start"

TILE_MAP = {}

WEIGHTS = {
    2: 1,
    3: 1,
    4: 1,
    5: 3,
    6: 1,
}

ITEM_WEIGHTS = {
    "Bush": 1,
    # TODO
}

FONT = pygame.font.SysFont("Arial", 256)

MAIN_CHARACTER_FOLDER = "Assets/Tiles/Characters/Main"

WEIGHTED_MAP = [key for key, value in WEIGHTS.items() for _ in range(value)]
FPS = 60
