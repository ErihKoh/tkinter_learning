import tkinter as tk
from random import shuffle


class MyButton(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=2, height=2, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0

    def __repr__(self):
        return f"MyButton x={self.x}, y={self.y}, num={self.number}, mine={self.is_mine}"


class MineSweeper:
    root = tk.Tk()

    ROWS = 10
    COLUMNS = 7
    MINES = 15

    def __init__(self):
        self.buttons = []

        for row in range(MineSweeper.ROWS + 2):
            temp = []
            for col in range(MineSweeper.COLUMNS + 2):
                btn = MyButton(MineSweeper.root, x=row, y=col)
                btn.config(command=lambda button=btn: self.click_btn(button))
                temp.append(btn)
            self.buttons.append(temp)

    def click_btn(self, clicked_btn: MyButton):
        if clicked_btn.is_mine:
            clicked_btn.config(text='*', highlightbackground="red", disabledforeground='black')
        else:
            clicked_btn.config(text=clicked_btn.number, disabledforeground='black')
        clicked_btn.config(state='disabled')

    def create_widgets(self):
        for row in range(1, MineSweeper.ROWS + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                btn.grid(row=row, column=col)

    def open_all_btn(self):
        for row in range(MineSweeper.ROWS + 2):
            for col in range(MineSweeper.COLUMNS + 2):
                btn = self.buttons[row][col]
                if btn.is_mine:
                    btn.config(text='*', highlightbackground="red", disabledforeground='black')
                else:
                    btn.config(text=btn.count_bomb, disabledforeground='black')

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.count_mines_in_buttons()
        self.print()
        self.open_all_btn()
        MineSweeper.root.mainloop()

    def insert_mines(self):
        index_mines = MineSweeper.get_mines_places()
        count = 1
        for row in range(1, MineSweeper.ROWS + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1

    def print(self):
        for row_btn in self.buttons:
            print(row_btn)

    def count_mines_in_buttons(self):
        for row in range(1, MineSweeper.ROWS + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[row + row_dx][col + col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.ROWS * MineSweeper.COLUMNS + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


def main():
    game = MineSweeper()
    game.start()


if __name__ == '__main__':
    main()
