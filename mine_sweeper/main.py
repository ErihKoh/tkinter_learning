import tkinter as tk
from random import shuffle


class MyButton(tk.Button):
    def __init__(self, master, x, y, number,  *args, **kwargs):
        super(MyButton, self).__init__(master, width=2, height=2, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self):
        return f"MyButton x={self.x}, y={self.y}, num={self.number}, mine={self.is_mine}"


class MineSweeper:
    root = tk.Tk()

    ROWS = 10
    COLUMNS = 7
    MINES = 15

    def __init__(self):
        self.buttons = []
        count = 1

        for row in range(MineSweeper.ROWS):
            temp = []
            for col in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.root, x=row, y=col, number=count)
                temp.append(btn)
                count += 1
            self.buttons.append(temp)

    def create_widgets(self):
        for row in range(MineSweeper.ROWS):
            for col in range(MineSweeper.COLUMNS):
                btn = self.buttons[row][col]
                btn.grid(row=row, column=col)

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.print()
        MineSweeper.root.mainloop()

    def insert_mines(self):
        index_mines = MineSweeper.get_mines_places(self)
        print(index_mines)
        for row_btn in self.buttons:
            for btn in row_btn:
                if btn.number in index_mines:
                    btn.is_mine = True

    def print(self):
        for row_btn in self.buttons:
            print(row_btn)

    @staticmethod
    def get_mines_places(self):
        indexes = list(range(1, MineSweeper.ROWS * MineSweeper.COLUMNS + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


def main():
    game = MineSweeper()
    game.start()


if __name__ == '__main__':
    main()
