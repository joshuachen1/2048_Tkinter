from tkinter import Tk, Label, messagebox, Canvas, StringVar, SUNKEN, BOTTOM, X
import random
import copy

class Game:

    def __init__(self, master):
        self.root = master
        self.root.title("2048")

        # ***** Status Bar *****
        self.status_msg = StringVar()
        self.status_msg.set("")
        self.status_bar = Label(self.root, textvariable=self.status_msg, bd=1, relief=SUNKEN)
        self.status_bar.pack(side=BOTTOM, padx=2, fill=X)

        # ***** Bind Controls *****
        visual_board = Canvas(self.root, width=500, height=500)
        self.root.bind('<Key>', self.shift)
        visual_board.pack()

        # ***** Initialize Board State *****
        BOARD_SIZE = 4
        self.board = self.new_board(BOARD_SIZE)
        self.spawn_num()
        self.spawn_num()
        self.display_board()


    def new_board(self, size):
        return [[(' ') for i in range(size)] for i in range(size)]

    def display_board(self):
        for i in range(len(self.board)):
            print("|", self.board[i][0], self.board[i][1], self.board[i][2], self.board[i][3],"|")
        print()

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
                rand_x = random.randint(0, 3)
                rand_y = random.randint(0, 3)

                if self.board[rand_x][rand_y] == ' ':
                    probability = random.randint(0, 10)
                    
                    if probability < 8:
                        self.board[rand_x][rand_y] = 2
                    else:
                        self.board[rand_x][rand_y] = 4
                        
                    spawning_num = False

        if self.is_board_full():
            messagebox.showinfo("Game Over", "Game Over")

    def shift(self, event):

        board_updated = False

        # ***** Determine Arrow Key Pressed *****
        if event.keycode == 8124162:
            key = "left"
            board_updated = self.shift_board_left()
        elif event.keycode == 8189699:
            key = "right"
            board_updated = self.shift_board_right()
        elif event.keycode == 8320768:
            key = "up"
            self.shift_board_up()
        elif event.keycode == 8255233:
            key = "down"
            self.shift_board_down()
        else:
            pass

        print(key + " key pressed.")

        if not board_updated:
            print("no shift occurred")

        self.display_board()

        if board_updated:
            self.spawn_num()
            self.display_board()

    def shift_board_left(self):
        rows_list = self.rows_with_nums()
        rows_shift = False

        transitioning = True
        while transitioning:
            temp = copy.deepcopy(self.board)

            for j in range(len(rows_list)):
                row = rows_list[j]

                for j in range(0, 3):  # looking at everything starting from right side
                    if self.board[row][j] == ' ':
                        if self.board[row][j + 1] != ' ':
                            self.board[row][j] = self.board[row][j + 1]
                            self.board[row][j + 1] = ' '
                            rows_shift = True

            if temp == self.board:
                transitioning = False

        return self.merge_cells_left(rows_list, rows_shift)

    def merge_cells_left(self, rows_list: list(), rows_shift: bool):
        cells_merged = False

        for i in range(len(rows_list)):
            row = rows_list[i]

            if self.board[row][0] != ' ' and self.board[row][0] == self.board[row][1]:
                self.board[row][0] += self.board[row][1]
                self.board[row][1] = self.board[row][2]
                self.board[row][2] = self.board[row][3]
                self.board[row][3] = ' '
                cells_merged = True

            if self.board[row][1] != ' ' and self.board[row][1] == self.board[row][2]:
                self.board[row][1] += self.board[row][2]
                self.board[row][2] = self.board[row][3]
                self.board[row][3] = ' '
                cells_merged = True

            if self.board[row][2] != ' ' and self.board[row][2] == self.board[row][3]:
                self.board[row][2] += self.board[row][3]
                self.board[row][3] = ' '
                cells_merged = True

        return rows_shift or cells_merged

    def shift_board_right(self):
        rows_list = self.rows_with_nums()
        rows_shift = False

        transitioning = True
        while transitioning:
            temp = copy.deepcopy(self.board)

            for j in range(len(rows_list)):
                row = rows_list[j]

                for j in reversed(range(1, 4)):  # looking at everything starting from right side
                    if self.board[row][j] == ' ':
                        if self.board[row][j - 1] != ' ':
                            self.board[row][j] = self.board[row][j - 1]
                            self.board[row][j - 1] = ' '
                            rows_shift = True

            if temp == self.board:
                transitioning = False

        return self.merge_cells_right(rows_list, rows_shift)

    def merge_cells_right(self, rows_list: list(), rows_shift: bool):
        cells_merged = False

        for i in range(len(rows_list)):
            row = rows_list[i]

            if self.board[row][3] != ' ' and self.board[row][3] == self.board[row][2]:
                self.board[row][3] += self.board[row][2]
                self.board[row][2] = self.board[row][1]
                self.board[row][1] = self.board[row][0]
                self.board[row][0] = ' '
                cells_merged = True

            if self.board[row][2] != ' ' and self.board[row][2] == self.board[row][1]:
                self.board[row][2] += self.board[row][1]
                self.board[row][1] = self.board[row][0]
                self.board[row][0] = ' '
                cells_merged = True

            if self.board[row][1] != ' ' and self.board[row][1] == self.board[row][0]:
                self.board[row][1] += self.board[row][0]
                self.board[row][0] = ' '
                cells_merged = True

        return rows_shift or cells_merged

    def shift_board_up(self):
        pass

    def shift_board_down(self):
        pass

    def rows_with_nums(self):
        populated_rows = list()

        for i in range(len(self.board)):
            if self.board[i] != [' ', ' ', ' ', ' ']:
                populated_rows.append(i)

        # print(populated_rows)
        return populated_rows

root = Tk()
Game(root)
root.mainloop()
