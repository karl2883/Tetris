# Tetris
__author__ = "karl2883"
__date__ = "01.03.2021"

import pygame
from tetris.board import Board
from tetris.colors import *
from tetris.piece import Piece
from tetris.input_handler import check_input

pygame.init()

# important variables
WIDTH = 300
HEIGHT = 600
FPS = 30
run = True

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


board = Board(10, 20, 0, 0, WIDTH, HEIGHT)
current_piece = Piece("O", board)

frames = 0
left_timeout = 0
right_timeout = 0
rotating_right = False
rotating_left = False


while run:
    clock.tick(FPS)
    frames += 1
    if frames == 30:
        frames = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(BLACK)

    keys = pygame.key.get_pressed()
    left_timeout, right_timeout, fall_ready, rotating_left, rotating_right = check_input(left_timeout, right_timeout, keys, current_piece, rotating_left, rotating_right)
    if not frames % 15 or fall_ready:
        if not current_piece.fall():
            current_piece = Piece.generate_piece(board)
    current_piece.fill_in()
    board.draw(win)
    pygame.display.update()

pygame.quit()
