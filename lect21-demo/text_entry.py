# Simple program demonstrating entry functionality
from tkinter import Entry, Tk, Button, StringVar
from tkinter.messagebox import showinfo

root = Tk()
s = StringVar()


def show_popup():
    showinfo(message=f"{s.get()} was entered")


button = Button(root, text="Click me", command=show_popup)
entry = Entry(root, textvariable=s)
button.pack()
entry.pack()

root.mainloop()

