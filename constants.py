import pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
RED = (255, 255, 255)
BLUE = (0, 0, 128)
GREEN = (0, 255, 0)

# Screen
ORIGINAL_TILE_SIZE = 16
SCALE = 3
TILE_SIZE = ORIGINAL_TILE_SIZE * SCALE

SCREEN_COLUMNS = 24
SCREEN_ROWS = 16

SCREEN_WIDTH = SCREEN_COLUMNS * TILE_SIZE
SCREEN_HEIGHT = SCREEN_ROWS * TILE_SIZE

# Fonts
GAP_WORD = 21
INCONSOLATA_SMALL_FONT = pygame.font.Font(
    "fonts/Inconsolata-VariableFont_wdth,wght.ttf", 21)
