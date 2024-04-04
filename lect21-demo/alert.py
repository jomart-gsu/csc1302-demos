# Simple program demonstrating showinfo() functionality
from tkinter import Button, Tk
from tkinter.messagebox import showinfo

root = Tk()


def show_popup():
    showinfo(message="Button was clicked")


button = Button(root, text="Click me", command=show_popup)
button.pack()

root.mainloop()

