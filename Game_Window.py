#!/usr/bin/env python
"""Provides GameWindow class for the user to interact with.

"""

from tkinter import Tk, Label, StringVar, SUNKEN
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

        # ***** Scoreboard *****
        self.points = StringVar()
        self.points.set("Points\n--------\n{}".format(self.game.score))
        point_counter = Label(self.root, textvariable=self.points, bd=1, relief=SUNKEN, fg="white", bg="brown")
        point_counter.grid(row=0, column=0)

        self.high_score = StringVar()
        self.high_score.set("Hi-Score\n--------\n{}".format(0))
        hs_counter = Label(self.root, textvariable=self.high_score, bd=1, relief=SUNKEN, fg="white", bg="brown")
        hs_counter.grid(row=0, column=8)

        # ***** Bind Controls *****
        self.root.bind('<Key>', self.determine_move)

        # ***** Tiles Canvas *****
        self.value00 = StringVar()
        self.value00.set("")
        tile00 = Label(self.root, textvariable=self.value00, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile00.grid(row=2, column=2)

        self.value01 = StringVar()
        self.value01.set("")
        tile01 = Label(self.root, textvariable=self.value01, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile01.grid(row=2, column=3)

        self.value02 = StringVar()
        self.value02.set("")
        tile02 = Label(self.root, textvariable=self.value02, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile02.grid(row=2, column=4)

        self.value03 = StringVar()
        self.value03.set("")
        tile03 = Label(self.root, textvariable=self.value03, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile03.grid(row=2, column=5)

        self.value10 = StringVar()
        self.value10.set("")
        tile10 = Label(self.root, textvariable=self.value10, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile10.grid(row=3, column=2)

        self.value11 = StringVar()
        self.value11.set("")
        tile11 = Label(self.root, textvariable=self.value11, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile11.grid(row=3, column=3)

        self.value12 = StringVar()
        self.value12.set("")
        tile12 = Label(self.root, textvariable=self.value12, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile12.grid(row=3, column=4)

        self.value13 = StringVar()
        self.value13.set("")
        tile13 = Label(self.root, textvariable=self.value13, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile13.grid(row=3, column=5)

        self.value20 = StringVar()
        self.value20.set("")
        tile20 = Label(self.root, textvariable=self.value20, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile20.grid(row=4, column=2)

        self.value21 = StringVar()
        self.value21.set("")
        tile21 = Label(self.root, textvariable=self.value21, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile21.grid(row=4, column=3)

        self.value22 = StringVar()
        self.value22.set("")
        tile22 = Label(self.root, textvariable=self.value22, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile22.grid(row=4, column=4)

        self.value23 = StringVar()
        self.value23.set("")
        tile23 = Label(self.root, textvariable=self.value23, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile23.grid(row=4, column=5)

        self.value30 = StringVar()
        self.value30.set("")
        tile30 = Label(self.root, textvariable=self.value30, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile30.grid(row=5, column=2)

        self.value31 = StringVar()
        self.value31.set("")
        tile31 = Label(self.root, textvariable=self.value31, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile31.grid(row=5, column=3)

        self.value32 = StringVar()
        self.value32.set("")
        tile32 = Label(self.root, textvariable=self.value32, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile32.grid(row=5, column=4)

        self.value33 = StringVar()
        self.value33.set("")
        tile33 = Label(self.root, textvariable=self.value33, bd=1, relief=SUNKEN, bg="gray", height=4, width=6)
        tile33.grid(row=5, column=5)

        self.display_board()

    def determine_move(self, event):
        board_updated = False

        # ***** Determine Arrow Key Pressed *****
        if event.keycode == 8124162:
            board_updated = self.game.shift_board_left()
        elif event.keycode == 8189699:
            board_updated = self.game.shift_board_right()
        elif event.keycode == 8320768:
            board_updated = self.game.shift_board_up()
        elif event.keycode == 8255233:
            board_updated = self.game.shift_board_down()
        else:
            pass

        self.display_board()
        self.points.set("Points\n--------\n{}".format(self.game.score))

        if board_updated:
            self.game.spawn_num()
            self.display_board()

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


if __name__ == '__main__':
    root = Tk()
    g = GameWindow(root)
    root.mainloop()
