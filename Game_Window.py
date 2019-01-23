from tkinter import Tk, Label, Canvas, StringVar, SUNKEN, BOTTOM, X
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

        # ***** Board Canvas *****
        # self.tile00 = Label(visual_board, width=100, height=100)
        # self.tile00.grid(row=0, column=0)

        self.display_board()

    def determine_move(self, event):
        board_updated = False

        # ***** Determine Arrow Key Pressed *****
        if event.keycode == 8124162:
            status = "Shift Left"
            board_updated = self.game.shift_board_left()
        elif event.keycode == 8189699:
            status = "Shift Right"
            board_updated = self.game.shift_board_right()
        elif event.keycode == 8320768:
            status = "Shift Up"
            board_updated = self.game.shift_board_up()
        elif event.keycode == 8255233:
            status = "Shift Down"
            board_updated = self.game.shift_board_down()
        else:
            pass

        if not board_updated:
            status = "No Shift Occurred"

        self.status_msg.set(status)

        self.display_board()

        if board_updated:
            self.game.spawn_num()
            self.display_board()

    def display_board(self):
        # Tkinter Display
        

        # Console Display
        for i in range(len(self.game.board)):
            print("|", self.game.board[i][0], self.game.board[i][1], self.game.board[i][2], self.game.board[i][3], "|")
        print()


if __name__ == '__main__':
    root = Tk()
    g = GameWindow(root)
    root.mainloop()
