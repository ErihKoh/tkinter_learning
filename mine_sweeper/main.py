import tkinter as tk

root = tk.Tk()

ROWS = 5
COLUMNS = 7


def create_btn():
    buttons = []

    for row in range(ROWS):
        temp = []
        for col in range(COLUMNS):
            btn = tk.Button(root, width=2, height=2, font='Calibri 15 bold')
            temp.append(btn)
        buttons.append(temp)
    return buttons


def grid_btn(buttons):
    for row in range(ROWS):
        for col in range(COLUMNS):
            btn = buttons[row][col]
            btn.grid(row=row, column=col)


def main():
    buttons = create_btn()
    grid_btn(buttons)

    root.mainloop()


if __name__ == '__main__':
    main()
