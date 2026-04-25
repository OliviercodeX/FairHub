#Constantes
import pygame
from pathlib import Path

# pygame.init()  # Remover, se hace en menu.py
pygame.font.init()

#COLORES
# Colores básicos
WHITE       = (255, 255, 255)
BLACK       = (0, 0, 0)
GRAY        = (128, 128, 128)
LIGHT_GRAY  = (200, 200, 200)
DARK_GRAY   = (50, 50, 50)

RED     = (220, 53, 69)
GREEN   = (40, 167, 69)
BLUE    = (0, 123, 255)
YELLOW  = (255, 193, 7)
ORANGE  = (255, 159, 64)
PURPLE  = (111, 66, 193)
CYAN    = (23, 162, 184)

BACKGROUND        = (30, 30, 30)
PANEL             = (45, 45, 45)
BUTTON_NORMAL     = (70, 130, 180)
BUTTON_HOVER      = (100, 149, 237)
BUTTON_PRESSED    = (65, 105, 225)
TEXT_PRIMARY      = (240, 240, 240)
TEXT_SECONDARY    = (180, 180, 180)

#Tamaño de pantalla
WIDTH, HEIGHT = 800, 600

#Fuentes y tamaños
FONT_SMALL_ES = pygame.font.SysFont("timesnewroman", 12)
FONT_SMALL  = pygame.font.SysFont("timesnewroman", 18)
FONT_NORMAL = pygame.font.SysFont("timesnewroman", 22)
FONT_MEDIUM = pygame.font.SysFont("timesnewroman", 28)
FONT_LARGE  = pygame.font.SysFont('timesnewroman' , 36)
FONT_TITLE  = pygame.font.SysFont("timesnewroman", 43)

ruta_image = Path(__file__).parent.parent / 'data' / 'assets' / 'image' / 'church_brand.jpeg'
