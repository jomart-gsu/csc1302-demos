from tkinter import Tk, Label, RAISED, Button, Frame, TOP, BOTTOM

root = Tk()

labels = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"],
]

input_text = Label(root, text="")
input_text.pack(side=TOP)
frame = Frame(root)
frame.pack(side=BOTTOM)

for r in range(4):
    for c in range(3):
        button = Button(
            frame,
            text=labels[r][c],
            padx=10,
            relief=RAISED,
            command=lambda num=labels[r][c]: input_text.config(text=input_text["text"] + num)
        )
        button.grid(row=r, column=c)

root.mainloop()