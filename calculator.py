import tkinter as tk

root = tk.Tk()
root.geometry(f"240x260+100+200")
root['bg'] = '#33ffe6'
root.title('Calculator')

calc = tk.Entry(root, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.grid(row=0, column=0, columnspan=3, stick='we')


def add_digit(digit):
    value = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, value)




tk.Button(text='1', bd=5, font=('Arial', 13),  command=lambda: add_digit(1)).grid(row=1, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='2', bd=5, font=('Arial', 13),  command=lambda: add_digit(2)).grid(row=1, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='3', bd=5, font=('Arial', 13),  command=lambda: add_digit(3)).grid(row=1, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='4', bd=5, font=('Arial', 13),  command=lambda: add_digit(4)).grid(row=2, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='5', bd=5, font=('Arial', 13),  command=lambda: add_digit(5)).grid(row=2, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='6', bd=5, font=('Arial', 13),  command=lambda: add_digit(6)).grid(row=2, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='7', bd=5, font=('Arial', 13),  command=lambda: add_digit(7)).grid(row=3, column=0, stick='wens', padx=5, pady=5)
tk.Button(text='8', bd=5, font=('Arial', 13),  command=lambda: add_digit(8)).grid(row=3, column=1, stick='wens', padx=5, pady=5)
tk.Button(text='9', bd=5, font=('Arial', 13),  command=lambda: add_digit(9)).grid(row=3, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='0', bd=5, font=('Arial', 13),  command=lambda: add_digit(0)).grid(row=4, column=0, stick='wens', padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

root.mainloop()
