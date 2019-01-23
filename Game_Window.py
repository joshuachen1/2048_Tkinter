from tkinter import Tk, Label, messagebox, Canvas, StringVar, SUNKEN, BOTTOM, X
import Game_Mechanics


class GameWindow:

    def __init__(self, master):
        self.game = Game_Mechanics.Game()

        self.root = master
        self.root.title("2048")

        # ***** Status Bar *****
        self.status_msg = StringVar()
        self.status_msg.set("")
        self.status_bar = Label(self.root, textvariable=self.status_msg, bd=1, relief=SUNKEN)
        self.status_bar.pack(side=BOTTOM, padx=2, fill=X)

        # ***** Bind Controls *****
        visual_board = Canvas(self.root, width=500, height=500)
        self.root.bind('<Key>', self.determine_move)
        visual_board.pack()

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

        if not board_updated:
            print("no shift occurred")

        self.display_board()

        if board_updated:
            self.game.spawn_num()
            self.display_board()

    def display_board(self):
        for i in range(len(self.game.board)):
            print("|", self.game.board[i][0], self.game.board[i][1], self.game.board[i][2], self.game.board[i][3], "|")
        print()



root = Tk()
g = GameWindow(root)
root.mainloop()