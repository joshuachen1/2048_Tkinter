import random
import copy


class Game:

    def __init__(self):
        # ***** Initialize Board State *****
        BOARD_SIZE = 4
        self.board = self.new_board(BOARD_SIZE)
        self.spawn_num()
        self.spawn_num()

        self.score = 0

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
                    probability = random.randint(0, 10)
                    
                    if probability < 8:
                        self.board[rand_r][rand_c] = 2
                    else:
                        self.board[rand_r][rand_c] = 4
                        
                    spawning_num = False

    def shift_board_left(self):
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
                cells_merged = True

            if self.board[row][1] != ' ' and self.board[row][1] == self.board[row][2]:
                self.board[row][1] += self.board[row][2]
                self.board[row][2] = self.board[row][3]
                self.board[row][3] = ' '
                self.score += self.board[row][1]
                cells_merged = True

            if self.board[row][2] != ' ' and self.board[row][2] == self.board[row][3]:
                self.board[row][2] += self.board[row][3]
                self.board[row][3] = ' '
                self.score += self.board[row][2]
                cells_merged = True

        return rows_shifted or cells_merged

    def shift_board_right(self):
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
                cells_merged = True

            if self.board[row][2] != ' ' and self.board[row][2] == self.board[row][1]:
                self.board[row][2] += self.board[row][1]
                self.board[row][1] = self.board[row][0]
                self.board[row][0] = ' '
                self.score += self.board[row][2]
                cells_merged = True

            if self.board[row][1] != ' ' and self.board[row][1] == self.board[row][0]:
                self.board[row][1] += self.board[row][0]
                self.board[row][0] = ' '
                self.score += self.board[row][1]
                cells_merged = True

        return rows_shifted or cells_merged

    def shift_board_up(self):
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
                cells_merged = True

            if self.board[1][col] != ' ' and self.board[1][col] == self.board[2][col]:
                self.board[1][col] += self.board[2][col]
                self.board[2][col] = self.board[3][col]
                self.board[3][col] = ' '
                self.score += self.board[1][col]
                cells_merged = True

            if self.board[2][col] != ' ' and self.board[2][col] == self.board[3][col]:
                self.board[2][col] += self.board[3][col]
                self.board[3][col] = ' '
                self.score += self.board[2][col]
                cells_merged = True

        return cols_shifted or cells_merged

    def shift_board_down(self):
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
                cells_merged = True

            if self.board[2][col] != ' ' and self.board[2][col] == self.board[1][col]:
                self.board[2][col] += self.board[1][col]
                self.board[1][col] = self.board[0][col]
                self.board[0][col] = ' '
                self.score += self.board[2][col]
                cells_merged = True

            if self.board[1][col] != ' ' and self.board[1][col] == self.board[0][col]:
                self.board[1][col] += self.board[0][col]
                self.board[0][col] = ' '
                self.score += self.board[1][col]
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
