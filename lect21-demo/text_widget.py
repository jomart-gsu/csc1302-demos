# Simple program demonstrating Text
from tkinter import Text, Tk, Button

root = Tk()
text = Text(root, width=40, height=20)
text.pack()
line_counter = 1


def add_line():
    global line_counter
    text.insert('end', f'\nThis is line {line_counter}')
    line_counter += 1


button = Button(text='Add a line', command=add_line)
button.pack()

root.mainloop()

