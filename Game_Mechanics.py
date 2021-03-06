#!/usr/bin/env python
"""Provides Game class for the mechanics of the game.

"""

import random
import copy

__author__ = "Joshua Chen, Allyson Yamasaki"
__credits__ = ["Joshua Chen", "Allyson Yamasaki"]


class Game:

    def __init__(self):
        # ***** Initialize Board State *****
        self.BOARD_SIZE = 4
        self.board = self.new_board(self.BOARD_SIZE)
        self.spawn_num()
        self.spawn_num()

        self.score = 0
        self.points_earned = 0
        self.game_over = False
        self.victory = False

    def new_board(self, size):
        return [[(' ') for i in range(size)] for i in range(size)]

    def is_board_full(self):
        board_full = True

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == ' ':
                    board_full = False
                    break

        return board_full

    def spawn_num(self):
        if not self.is_board_full():
            spawning_num = True

            while spawning_num:
                rand_r = random.randint(0, 3)
                rand_c = random.randint(0, 3)

                if self.board[rand_r][rand_c] == ' ':
                    probability = random.randint(0, 100)
                    
                    if probability < 95:
                        self.board[rand_r][rand_c] = 2
                    else:
                        self.board[rand_r][rand_c] = 4
                        
                    spawning_num = False

            if self.is_board_full() and self.is_game_over():
                self.game_over = True
                print("Game Over")
        else:
            if self.is_game_over():
                self.game_over = True
                print("Game Over")

    def shift_board_left(self):
        if not self.game_over:
            rows_list = self.rows_with_nums()
            rows_shifted = False

            transitioning = True
            while transitioning:
                temp = copy.deepcopy(self.board)

                for j in range(len(rows_list)):
                    row = rows_list[j]

                    for k in range(0, 3):  # looking at everything starting from left side
                        if self.board[row][k] == ' ':
                            if self.board[row][k + 1] != ' ':
                                self.board[row][k] = self.board[row][k + 1]
                                self.board[row][k + 1] = ' '
                                rows_shifted = True

                if temp == self.board:
                    transitioning = False

            return self.merge_cells_left(rows_list, rows_shifted)

    def merge_cells_left(self, rows_list: list(), rows_shifted: bool):
        cells_merged = False

        for i in range(len(rows_list)):
            row = rows_list[i]

            if self.board[row][0] != ' ' and self.board[row][0] == self.board[row][1]:
                self.board[row][0] += self.board[row][1]
                self.board[row][1] = self.board[row][2]
                self.board[row][2] = self.board[row][3]
                self.board[row][3] = ' '
                self.score += self.board[row][0]
                self.points_earned += self.board[row][0]
                cells_merged = True

            if self.board[row][1] != ' ' and self.board[row][1] == self.board[row][2]:
                self.board[row][1] += self.board[row][2]
                self.board[row][2] = self.board[row][3]
                self.board[row][3] = ' '
                self.score += self.board[row][1]
                self.points_earned += self.board[row][1]
                cells_merged = True

            if self.board[row][2] != ' ' and self.board[row][2] == self.board[row][3]:
                self.board[row][2] += self.board[row][3]
                self.board[row][3] = ' '
                self.score += self.board[row][2]
                self.points_earned += self.board[row][2]
                cells_merged = True

        return rows_shifted or cells_merged

    def shift_board_right(self):
        if not self.game_over:
            rows_list = self.rows_with_nums()
            rows_shifted = False

            transitioning = True
            while transitioning:
                temp = copy.deepcopy(self.board)

                for j in range(len(rows_list)):
                    row = rows_list[j]

                    for k in reversed(range(1, 4)):  # looking at everything starting from right side
                        if self.board[row][k] == ' ':
                            if self.board[row][k - 1] != ' ':
                                self.board[row][k] = self.board[row][k - 1]
                                self.board[row][k - 1] = ' '
                                rows_shifted = True

                if temp == self.board:
                    transitioning = False

            return self.merge_cells_right(rows_list, rows_shifted)

    def merge_cells_right(self, rows_list: list(), rows_shifted: bool):
        cells_merged = False

        for i in range(len(rows_list)):
            row = rows_list[i]

            if self.board[row][3] != ' ' and self.board[row][3] == self.board[row][2]:
                self.board[row][3] += self.board[row][2]
                self.board[row][2] = self.board[row][1]
                self.board[row][1] = self.board[row][0]
                self.board[row][0] = ' '
                self.score += self.board[row][3]
                self.points_earned += self.board[row][3]
                cells_merged = True

            if self.board[row][2] != ' ' and self.board[row][2] == self.board[row][1]:
                self.board[row][2] += self.board[row][1]
                self.board[row][1] = self.board[row][0]
                self.board[row][0] = ' '
                self.score += self.board[row][2]
                self.points_earned += self.board[row][2]
                cells_merged = True

            if self.board[row][1] != ' ' and self.board[row][1] == self.board[row][0]:
                self.board[row][1] += self.board[row][0]
                self.board[row][0] = ' '
                self.score += self.board[row][1]
                self.points_earned += self.board[row][1]
                cells_merged = True

        return rows_shifted or cells_merged

    def shift_board_up(self):
        if not self.game_over:
            cols_list = self.cols_with_nums()
            cols_shifted = False

            transitioning = True
            while transitioning:
                temp = copy.deepcopy(self.board)

                for j in range(len(cols_list)):
                    col = cols_list[j]

                    for k in range(0, 3):
                        if self.board[k][col] == ' ':
                            if self.board[k + 1][col] != ' ':
                                self.board[k][col] = self.board[k + 1][col]
                                self.board[k + 1][col] = ' '
                                cols_shifted = True

                if temp == self.board:
                    transitioning = False

            return self.merge_cells_up(self.cols_with_nums(), cols_shifted)

    def merge_cells_up(self, cols_list: list(), cols_shifted: bool):
        cells_merged = False

        for i in range(len(cols_list)):
            col = cols_list[i]

            if self.board[0][col] != ' ' and self.board[0][col] == self.board[1][col]:
                self.board[0][col] += self.board[1][col]
                self.board[1][col] = self.board[2][col]
                self.board[2][col] = self.board[3][col]
                self.board[3][col] = ' '
                self.score += self.board[0][col]
                self.points_earned += self.board[0][col]
                cells_merged = True

            if self.board[1][col] != ' ' and self.board[1][col] == self.board[2][col]:
                self.board[1][col] += self.board[2][col]
                self.board[2][col] = self.board[3][col]
                self.board[3][col] = ' '
                self.score += self.board[1][col]
                self.points_earned += self.board[1][col]
                cells_merged = True

            if self.board[2][col] != ' ' and self.board[2][col] == self.board[3][col]:
                self.board[2][col] += self.board[3][col]
                self.board[3][col] = ' '
                self.score += self.board[2][col]
                self.points_earned += self.board[2][col]
                cells_merged = True

        return cols_shifted or cells_merged

    def shift_board_down(self):
        if not self.game_over:
            cols_list = self.cols_with_nums()
            cols_shifted = False

            transitioning = True
            while transitioning:
                temp = copy.deepcopy(self.board)

                for j in range(len(cols_list)):
                    col = cols_list[j]

                    for j in reversed(range(1, 4)):  # looking at everything starting from right side
                        if self.board[j][col] == ' ':
                            if self.board[j-1][col] != ' ':
                                self.board[j][col] = self.board[j - 1][col]
                                self.board[j - 1][col] = ' '
                                cols_shifted = True

                if temp == self.board:
                    transitioning = False

            return self.merge_cells_down(cols_list, cols_shifted)

    def merge_cells_down(self, cols_list: list(), cols_shifted: bool):
        cells_merged = False

        for i in range(len(cols_list)):
            col = cols_list[i]

            if self.board[3][col] != ' ' and self.board[3][col] == self.board[2][col]:
                self.board[3][col] += self.board[2][col]
                self.board[2][col] = self.board[1][col]
                self.board[1][col] = self.board[0][col]
                self.board[0][col] = ' '
                self.score += self.board[3][col]
                self.points_earned += self.board[3][col]
                cells_merged = True

            if self.board[2][col] != ' ' and self.board[2][col] == self.board[1][col]:
                self.board[2][col] += self.board[1][col]
                self.board[1][col] = self.board[0][col]
                self.board[0][col] = ' '
                self.score += self.board[2][col]
                self.points_earned += self.board[2][col]
                cells_merged = True

            if self.board[1][col] != ' ' and self.board[1][col] == self.board[0][col]:
                self.board[1][col] += self.board[0][col]
                self.board[0][col] = ' '
                self.score += self.board[1][col]
                self.points_earned += self.board[1][col]
                cells_merged = True

        return cols_shifted or cells_merged

    def rows_with_nums(self):
        populated_rows = list()

        for row in range(len(self.board)):
            if self.board[row] != [0, 0, 0, 0]:
                populated_rows.append(row)

        # print(populated_rows)
        return populated_rows

    def cols_with_nums(self):
        populated_cols = list()

        for col in range(len(self.board)):
            if not (self.board[0][col] == ' ' and self.board[1][col] == ' ' and self.board[2][col] == ' ' and self.board[3][col] == ' '):
                populated_cols.append(col)

        # print(populated_cols)
        return populated_cols

    def did_player_win(self):
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.board[i][j] == 2048:
                    self.victory = True

    def is_game_over(self):
        # Every Tile is Full
        no_possible_moves = True

        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                curr_tile = self.board[row][col]

                try:
                    # Above
                    if curr_tile == self.board[row - 1][col]:
                        no_possible_moves = False
                except IndexError:
                    pass

                try:
                    # Left
                    if curr_tile == self.board[row][col - 1]:
                        no_possible_moves = False
                except IndexError:
                    pass

                try:
                    # Right
                    if curr_tile == self.board[row][col + 1]:
                        no_possible_moves = False
                except IndexError:
                    pass

                try:
                    # Below
                    if curr_tile == self.board[row + 1][col]:
                        no_possible_moves = False
                except IndexError:
                    pass

                if not no_possible_moves:
                    break

        return no_possible_moves

    def reset_points(self):
        self.points_earned = 0

    def soft_reset(self):
        self.board = self.new_board(self.BOARD_SIZE)
        self.score = 0
        self.reset_points()
        self.spawn_num()
        self.spawn_num()
