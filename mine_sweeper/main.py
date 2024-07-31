import tkinter as tk
from tkinter.messagebox import showinfo, showerror
from random import shuffle

from mine_sweeper.colors import colors
from mine_sweeper.my_button import MyButton


class MineSweeper:
    root = tk.Tk()

    ROWS = 10
    COLUMNS = 7
    MINES = 10
    IS_GAME_OVER = False
    IS_FIRST_CLICK = True

    def __init__(self):
        self.buttons = []

        for row in range(MineSweeper.ROWS + 2):
            temp = []
            for col in range(MineSweeper.COLUMNS + 2):
                btn = MyButton(MineSweeper.root, x=row, y=col)
                btn.config(command=lambda button=btn: self.click_btn(button))
                btn.bind('<Button-2>', self.right_click)
                temp.append(btn)
            self.buttons.append(temp)

    def right_click(self, event):
        if MineSweeper.IS_GAME_OVER:
            return
        cur_btn = event.widget

        if cur_btn['state'] == 'normal':
            cur_btn['state'] = 'disabled'
            cur_btn['text'] = '🚩'
        elif cur_btn['text'] == '🚩':
            cur_btn['text'] = ''
            cur_btn['state'] = 'normal'

    def click_btn(self, clicked_btn: MyButton):
        if MineSweeper.IS_GAME_OVER:
            return

        if MineSweeper.IS_FIRST_CLICK:
            self.insert_mines(clicked_btn.number)
            self.count_mines_in_buttons()
            self.print()
            MineSweeper.IS_FIRST_CLICK = False

        if clicked_btn.is_mine:
            clicked_btn.config(text='*', highlightbackground="red", disabledforeground='black')
            clicked_btn.is_open = True
            MineSweeper.IS_GAME_OVER = True
            showinfo('Game over', 'The game is over, you lost')
            for row in range(1, MineSweeper.ROWS + 1):
                for col in range(1, MineSweeper.COLUMNS + 1):
                    btn = self.buttons[row][col]
                    if btn.is_mine:
                        btn['text'] = '*'

        else:
            color = colors.get(clicked_btn.count_bomb, 'black')
            if clicked_btn.count_bomb:
                clicked_btn.config(text=clicked_btn.count_bomb, disabledforeground=color)
                clicked_btn.is_open = True
            else:
                self.breadth_first_search(clicked_btn)
        clicked_btn.config(state='disabled')
        clicked_btn.config(relief='sunken')

    def breadth_first_search(self, btn: MyButton):
        queue = [btn]

        while queue:
            current_btn = queue.pop()
            color = colors.get(current_btn.count_bomb, 'black')
            if current_btn.count_bomb:
                current_btn.config(text=current_btn.count_bomb, disabledforeground=color)
            else:
                current_btn.config(text='', disabledforeground=color)
            current_btn.is_open = True
            current_btn.config(state='disabled')
            current_btn.config(relief='sunken')

            if current_btn.count_bomb == 0:
                x, y = current_btn.x, current_btn.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        # if not abs(dx - dy) == 1:
                        #     continue

                        next_btn = self.buttons[x + dx][y + dy]

                        if not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.ROWS and \
                                1 <= next_btn.y <= MineSweeper.COLUMNS and next_btn not in queue:
                            queue.append(next_btn)

    def reload(self):
        [child.destroy() for child in self.root.winfo_children()]
        self.__init__()
        self.create_widgets()
        MineSweeper.IS_FIRST_CLICK = True
        MineSweeper.IS_GAME_OVER = False

    def create_settings_window(self):
        win_settings = tk.Toplevel(self.root)
        win_settings.wm_title('Settings')

        tk.Label(win_settings, text='Rows').grid(row=0, column=0)
        rows_entry = tk.Entry(win_settings)
        rows_entry.insert(0, str(MineSweeper.ROWS))
        rows_entry.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(win_settings, text='Columns').grid(row=1, column=0)
        columns_entry = tk.Entry(win_settings)
        columns_entry.insert(0, str(MineSweeper.COLUMNS))
        columns_entry.grid(row=1, column=1, padx=20, pady=20)

        tk.Label(win_settings, text='Mines').grid(row=2, column=0)
        mines_entry = tk.Entry(win_settings)
        mines_entry.insert(0, str(MineSweeper.MINES))
        mines_entry.grid(row=2, column=1, padx=20, pady=20)

        run_btn = tk.Button(win_settings, text='Run',
                            command=lambda: self.change_settings(rows_entry, columns_entry, mines_entry))

        run_btn.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

    def change_settings(self, rows: tk.Entry, columns: tk.Entry, mines: tk.Entry):
        try:
            int(rows.get()), int(columns.get()), int(mines.get())
        except ValueError:
            showerror('Error', 'You have to enter a number ')
            return

        MineSweeper.ROWS = int(rows.get())
        MineSweeper.COLUMNS = int(columns.get())
        MineSweeper.MINES = int(mines.get())
        self.reload()

    def create_widgets(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label='Play', command=self.reload)
        settings_menu.add_command(label='Settings', command=self.create_settings_window)
        settings_menu.add_command(label='Exit', command=self.root.destroy)
        menubar.add_cascade(label='File', menu=settings_menu)

        count = 1
        for row in range(1, MineSweeper.ROWS + 1):
            self.root.rowconfigure(index=row, weight=1)
            for col in range(1, MineSweeper.COLUMNS + 1):
                self.root.columnconfigure(index=col, weight=1)
                btn = self.buttons[row][col]
                btn.number = count
                btn.grid(row=row, column=col, stick='NWES')
                count += 1

    def open_all_btn(self):
        for row in range(MineSweeper.ROWS + 2):
            for col in range(MineSweeper.COLUMNS + 2):
                btn = self.buttons[row][col]
                if btn.is_mine:
                    btn.config(text='*', fg="red", disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb, fg=color)

    def start(self):
        self.create_widgets()
        # self.open_all_btn()
        MineSweeper.root.mainloop()

    def insert_mines(self, number: int):
        index_mines = MineSweeper.get_mines_places(number)
        for row in range(1, MineSweeper.ROWS + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                if btn.number in index_mines:
                    btn.is_mine = True

    def print(self):
        for row in range(1, MineSweeper.ROWS + 1):
            for col in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[row][col]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

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
    def get_mines_places(exclude_number):
        indexes = list(range(1, MineSweeper.ROWS * MineSweeper.COLUMNS + 1))
        indexes.remove(exclude_number)
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


def main():
    game = MineSweeper()
    game.start()


if __name__ == '__main__':
    main()
