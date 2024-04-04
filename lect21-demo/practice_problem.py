from tkinter import Tk, Button, Entry, StringVar

root = Tk()

s = StringVar()
entry = Entry(root, textvariable=s)
button_list = []

def draw_buttons():
    global button_list
    button_list = []
    number_of_buttons = int(s.get())
    for i in range(number_of_buttons):
        new_button = Button(root, text="Delete me", command=lambda idx=i: button_list[idx].destroy())
        button_list.append(new_button)
        new_button.pack()

button = Button(root, text="Draw", command=draw_buttons)
entry.pack()
button.pack()

root.mainloop()