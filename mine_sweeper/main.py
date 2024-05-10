import tkinter as tk


class MineSweeper:
    root = tk.Tk()

    ROWS = 10
    COLUMNS = 7

    def __init__(self):
        self.buttons = []

        for row in range(MineSweeper.ROWS):
            temp = []
            for col in range(MineSweeper.COLUMNS):
                btn = tk.Button(MineSweeper.root, width=2, height=2, font='Calibri 15 bold')
                temp.append(btn)
            self.buttons.append(temp)

    def create_widgets(self):
        for row in range(MineSweeper.ROWS):
            for col in range(MineSweeper.COLUMNS):
                btn = self.buttons[row][col]
                btn.grid(row=row, column=col)

    def start(self):
        self.create_widgets()
        MineSweeper.root.mainloop()


def main():
    game = MineSweeper()

    game.start()


if __name__ == '__main__':
    main()
