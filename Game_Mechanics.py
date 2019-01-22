from tkinter import Tk, Label, Frame, Canvas, StringVar, SUNKEN, BOTTOM, X
import random


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
        self.board = self.new_board()
        self.spawn_num()
        self.spawn_num()
        self.display_board()


    def new_board(self):
        return [[(' ') for i in range(4)] for i in range(4)]

    def display_board(self):
        for i in range(4):
            print("|", self.board[i][0], self.board[i][1], self.board[i][2], self.board[i][3],"|")
        print()

    def is_board_full(self):
        board_full = True

        for i in range(4):
            for j in range(4):
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
                    self.board[rand_x][rand_y] = (2 * random.randint(1, 2))  # Spawn either 2 or 4
                    spawning_num = False

    def shift(self, event):

        # Determine shift
        if event.keycode == 8124162:
            shift = "left"
        elif event.keycode == 8189699:
            shift = "right"
        elif event.keycode == 8320768:
            shift = "up"
        elif event.keycode == 8255233:
            shift = "down"
        else:
            shift = "no shift"

        if shift == "no shift":
            pass

        else:
            # Shift board

            print ("shift: " + shift)
            self.display_board()
            self.spawn_num()
            self.display_board()




root = Tk()
Game(root)
root.mainloop()
