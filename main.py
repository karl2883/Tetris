# Tetris
__author__ = "karl2883"
__date__ = "01.03.2021"


# Done with pygame
import pygame
pygame.init()

# Constants for colors
from tetris.colors import *

import random
import time

# important variables
WIDTH = 600
HEIGHT = 600

win = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Tetris")
