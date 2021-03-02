from tetris.colors import *
import random


class Piece:

    piece_color_dict = {
        "I": [BLUE, [[-2, 0], [-1, 0], [0, 0], [1, 0]]],
        "O": [RED, [[-1, 0], [0, 0], [-1, 1], [0, 1]]],
        "T": [YELLOW, [[-1, 0], [0, 0], [1, 0], [0, -1]]],
        "J": [GREEN, [[-1, 0], [0, 0], [1, 0], [-1, -1]]],
        "L": [ORANGE, [[-1, 0], [0, 0], [1, 0], [1, -1]]],
        "S": [WHITE, [[-1, 0], [0, 0], [0, -1], [1, -1]]],
        "Z": [PURPLE, [[-1, -1], [0, -1], [0, 0], [1, 0]]]
    }

    @classmethod
    def generate_piece(cls, board):
        form_list = ["I", "O", "T", "J", "L", "S", "Z"]
        form = form_list[random.randint(0, 6)]
        p = Piece(form, board)
        pos = [[p.x + piece[0], p.y + piece[1]] for piece in p.pieces]
        for piece in pos:
            if p.board.grid[piece[1]][piece[0]]:
                return False
        return p

    def __init__(self, form, board):
        self.form = form
        self.color = Piece.piece_color_dict[self.form][0]
        self.pieces = Piece.piece_color_dict[self.form][1]
        self.board = board
        self.y = 1
        if self.form == "O" or self.form == "I":
            self.y = 0
        self.x = board.cells_x // 2

    def check_position(self, position):
        for piece in position:
            if piece[0] >= self.board.cells_x or piece[0] < 0 or piece[1] >= self.board.cells_y:
                return False
            elif self.board.grid[piece[1]][piece[0]] and [piece[0] - self.x, piece[1] - self.y] not in self.pieces:
                return False
        return True

    def fill_in(self):
        for piece in self.pieces:
            self.board.grid[self.y + piece[1]][self.x + piece[0]] = self.color

    def delete_from_board(self):
        for piece in self.pieces:
            self.board.grid[self.y + piece[1]][self.x + piece[0]] = None

    def move_left(self):
        new_position = [[self.x + piece[0] - 1, self.y + piece[1]] for piece in self.pieces]
        if not self.check_position(new_position):
            return False
        self.delete_from_board()
        self.x -= 1
        return True

    def move_right(self):
        new_position = [[self.x + piece[0] + 1, self.y + piece[1]] for piece in self.pieces]
        if not self.check_position(new_position):
            return False
        self.delete_from_board()
        self.x += 1
        return True

    def rotate_left(self):
        if self.form == "O":
            return
        # special case
        elif self.form == "I":
            i_positions = [
                [[-2, 0], [-1, 0], [0, 0], [1, 0]],
                [[-1, -1], [-1, 0], [-1, 1], [-1, 2]],
                [[-2, 1], [-1, 1], [0, 1], [1, 1]],
                [[0, -1], [0, 0], [0, 1], [0, 2]]
            ]
            if self.pieces[0][0] == 0:
                pieces = i_positions[2]
            elif self.pieces[0][0] == -1:
                pieces = i_positions[0]
            elif self.pieces[0][1] == 0:
                pieces = i_positions[3]
            else:
                pieces = i_positions[1]
            new_position = [[self.x + piece[0], self.y + piece[1]] for piece in pieces]
            if not self.check_position(new_position):
                return
            else:
                self.delete_from_board()
                self.pieces = pieces.copy()
                self.fill_in()
        else:
            new_position = [[self.x - piece[1], self.y + piece[0]] for piece in self.pieces]
            if not self.check_position(new_position):
                return
            else:
                self.delete_from_board()
                self.pieces = [[-piece[1], piece[0]] for piece in self.pieces]
                self.fill_in()

    def rotate_right(self):
        if self.form == "O":
            return
        # special case
        elif self.form == "I":
            i_positions = [
                [[-2, 0], [-1, 0], [0, 0], [1, 0]],
                [[-1, -1], [-1, 0], [-1, 1], [-1, 2]],
                [[-2, 1], [-1, 1], [0, 1], [1, 1]],
                [[0, -1], [0, 0], [0, 1], [0, 2]]
            ]
            if self.pieces[0][0] == 0:
                pieces = i_positions[0]
            elif self.pieces[0][0] == -1:
                pieces = i_positions[2]
            elif self.pieces[0][1] == 0:
                pieces = i_positions[1]
            else:
                pieces = i_positions[3]
            new_position = [[self.x + piece[0], self.y + piece[1]] for piece in pieces]
            if not self.check_position(new_position):
                return
            else:
                self.delete_from_board()
                self.pieces = pieces.copy()
                self.fill_in()
        else:
            new_position = [[self.x + piece[1], self.y - piece[0]] for piece in self.pieces]
            if not self.check_position(new_position):
                return
            else:
                self.delete_from_board()
                self.pieces = [[piece[1], -piece[0]] for piece in self.pieces]
                self.fill_in()

    def fall(self):
        new_position = [[self.x + piece[0], self.y + piece[1] + 1] for piece in self.pieces]
        if not self.check_position(new_position):
            return False
        self.delete_from_board()
        self.y += 1
        self.fill_in()
        return True
