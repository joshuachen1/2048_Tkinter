#!/usr/bin/env python
"""Provides GameWindow class for the user to interact with.

"""

from tkinter import Tk, Menu, Label, Canvas, StringVar, SUNKEN, BOTTOM, X
import Game_Mechanics

__author__ = "Joshua Chen, Allyson Yamasaki"
__credits__ = ["Joshua Chen", "Allyson Yamasaki"]

#  ___   ___  _  _   ___
# |__ \ / _ \| || | / _ \
#    ) | | | | || || (_) |
#   / /| | | |__   _> _ <
#  / /_| |_| |  | || (_) |
# |____|\___/   |_| \___/
#


class GameWindow:

    def __init__(self, master):
        self.game = Game_Mechanics.Game()

        self.root = master
        self.root.title("2048")

        # ***** Menu *****
        main_menu = Menu(master)
        master.config(menu=main_menu)

        game_menu = Menu(main_menu)
        main_menu.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.new_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.quit)

        # ***** Scoreboard *****
        self.score = self.game.score
        self.points = StringVar()
        self.points.set("Points\n--------\n{}".format(self.score))
        point_counter = Label(self.root, textvariable=self.points, bd=1, relief=SUNKEN, fg="white", bg="brown")
        point_counter.grid(row=0, column=0)

        self.hi_score = 0
        self.high_score = StringVar()
        self.high_score.set("Hi-Score\n--------\n{}".format(self.hi_score))
        hs_counter = Label(self.root, textvariable=self.high_score, bd=1, relief=SUNKEN, fg="white", bg="brown")
        hs_counter.grid(row=0, column=8)

        # ***** Bind Controls *****
        self.root.bind('<Key>', self.determine_move)

        # ***** Tiles Canvas *****
        self.RGB = (255, 153, 102)  #ff9966
        self.create_tiles()

        # ***** Status Bar *****
        status_canvas = Canvas(self.root)
        status_canvas.grid(row=6, columnspan=10)
        self.status = StringVar()
        self.status.set("\tGAME START\t")
        self.status_bar = Label(status_canvas, textvariable=self.status, bd=1, relief=SUNKEN, )
        self.status_bar.pack(side=BOTTOM, padx=2, fill=X)

        self.display_board()

    def determine_move(self, event):
        board_updated = False

        # ***** Determine Arrow Key Pressed *****
        if event.keycode == 8124162 or event.keycode == 97:
            board_updated = self.game.shift_board_left()
        elif event.keycode == 8189699 or event.keycode == 100:
            board_updated = self.game.shift_board_right()
        elif event.keycode == 8320768 or event.keycode == 119:
            board_updated = self.game.shift_board_up()
        elif event.keycode == 8255233 or event.keycode == 115:
            board_updated = self.game.shift_board_down()
        else:
            pass

        self.display_board()

        self.update_counters()

        if board_updated:
            self.game.spawn_num()
            self.display_board()

    def create_tiles(self):
        self.value00 = StringVar()
        self.value00.set("")
        self.tile00 = Label(self.root, textvariable=self.value00, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile00.grid(row=2, column=2)

        self.value01 = StringVar()
        self.value01.set("")
        self.tile01 = Label(self.root, textvariable=self.value01, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile01.grid(row=2, column=3)

        self.value02 = StringVar()
        self.value02.set("")
        self.tile02 = Label(self.root, textvariable=self.value02, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile02.grid(row=2, column=4)

        self.value03 = StringVar()
        self.value03.set("")
        self.tile03 = Label(self.root, textvariable=self.value03, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile03.grid(row=2, column=5)

        self.value10 = StringVar()
        self.value10.set("")
        self.tile10 = Label(self.root, textvariable=self.value10, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile10.grid(row=3, column=2)

        self.value11 = StringVar()
        self.value11.set("")
        self.tile11 = Label(self.root, textvariable=self.value11, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile11.grid(row=3, column=3)

        self.value12 = StringVar()
        self.value12.set("")
        self.tile12 = Label(self.root, textvariable=self.value12, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile12.grid(row=3, column=4)

        self.value13 = StringVar()
        self.value13.set("")
        self.tile13 = Label(self.root, textvariable=self.value13, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile13.grid(row=3, column=5)

        self.value20 = StringVar()
        self.value20.set("")
        self.tile20 = Label(self.root, textvariable=self.value20, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile20.grid(row=4, column=2)

        self.value21 = StringVar()
        self.value21.set("")
        self.tile21 = Label(self.root, textvariable=self.value21, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile21.grid(row=4, column=3)

        self.value22 = StringVar()
        self.value22.set("")
        self.tile22 = Label(self.root, textvariable=self.value22, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile22.grid(row=4, column=4)

        self.value23 = StringVar()
        self.value23.set("")
        self.tile23 = Label(self.root, textvariable=self.value23, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile23.grid(row=4, column=5)

        self.value30 = StringVar()
        self.value30.set("")
        self.tile30 = Label(self.root, textvariable=self.value30, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile30.grid(row=5, column=2)

        self.value31 = StringVar()
        self.value31.set("")
        self.tile31 = Label(self.root, textvariable=self.value31, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile31.grid(row=5, column=3)

        self.value32 = StringVar()
        self.value32.set("")
        self.tile32 = Label(self.root, textvariable=self.value32, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile32.grid(row=5, column=4)

        self.value33 = StringVar()
        self.value33.set("")
        self.tile33 = Label(self.root, textvariable=self.value33, bd=1, relief=SUNKEN,
                            bg="#%02x%02x%02x" % self.RGB, height=4, width=6)
        self.tile33.grid(row=5, column=5)

    def display_board(self):
        # Tkinter Display
        self.value00.set("{}".format(self.game.board[0][0]))
        self.value01.set("{}".format(self.game.board[0][1]))
        self.value02.set("{}".format(self.game.board[0][2]))
        self.value03.set("{}".format(self.game.board[0][3]))
        self.value10.set("{}".format(self.game.board[1][0]))
        self.value11.set("{}".format(self.game.board[1][1]))
        self.value12.set("{}".format(self.game.board[1][2]))
        self.value13.set("{}".format(self.game.board[1][3]))
        self.value20.set("{}".format(self.game.board[2][0]))
        self.value21.set("{}".format(self.game.board[2][1]))
        self.value22.set("{}".format(self.game.board[2][2]))
        self.value23.set("{}".format(self.game.board[2][3]))
        self.value30.set("{}".format(self.game.board[3][0]))
        self.value31.set("{}".format(self.game.board[3][1]))
        self.value32.set("{}".format(self.game.board[3][2]))
        self.value33.set("{}".format(self.game.board[3][3]))

        # Console Display
        for i in range(len(self.game.board)):
            print("|", self.game.board[i][0], self.game.board[i][1], self.game.board[i][2], self.game.board[i][3], "|")
        print()

    def update_counters(self):
        if self.game.points_earned > 0:
            self.status.set("You got {} points!".format(self.game.points_earned))
        else:
            self.status.set("-----------------")

        self.game.reset_points()

        self.score = self.game.score
        self.points.set("Points\n--------\n{}".format(self.score))

    def new_game(self):
        if self.hi_score < self.score:
            self.hi_score = self.score
            self.high_score.set("Hi-Score\n--------\n{}".format(self.hi_score))

        self.score = 0
        self.game.soft_reset()
        self.display_board()
        self.points.set("Points\n--------\n{}".format(self.game.score))
        self.status.set("New Game Initiated")

    def quit(self):
        self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    g = GameWindow(root)
    root.mainloop()
