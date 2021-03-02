import pygame
from tetris.colors import *


class Board:
    def __init__(self, cells_x, cells_y, start_x, start_y, end_x, end_y):
        self.grid = []
        self.cells_x = cells_x
        self.cells_y = cells_y
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.cell_width = (end_x - start_x) // cells_x
        self.cell_height = (end_y - start_y) // cells_y
        for i in range(cells_y):
            self.grid.append([None] * cells_x)

    def check_full_lines(self):
        line_full = False
        for row_ind in range(len(self.grid)):
            if all(self.grid[row_ind]):
                line_full = True
                for new_row_ind in range(row_ind-1, 0, -1):
                    t = self.grid[new_row_ind].copy()
                    self.grid[new_row_ind+1] = t.copy()
        if line_full:
            return True
        return False

    def draw(self, window):
        # outlines
        for i in range(self.cells_x):
            pygame.draw.rect(window, GREY, (self.start_x + (i+1)*self.cell_width-1, self.start_y, 1, self.end_y - self.start_y))
        for i in range(self.cells_y):
            pygame.draw.rect(window, GREY, (self.start_x, self.start_y + (i+1)*self.cell_height-1, self.end_x - self.start_x, 1))
        # pieces
        for i in range(self.cells_y):
            for j in range(self.cells_x):
                if self.grid[i][j]:
                    pygame.draw.rect(window, self.grid[i][j], (j*self.cell_width, i*self.cell_height, self.cell_width-1, self.cell_height-1))
