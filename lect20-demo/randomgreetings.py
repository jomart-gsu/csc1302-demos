from tkinter import Tk, Button, Label
import random

root = Tk()

greetings = ["Hey", "Hello", "Hi", "Salutations", "Greetings"]
label = Label(root, text="Hey")
def update_label():
    new_label = random.choice(greetings)
    label.config(text=new_label)

button = Button(root, text="New Greeting", command=update_label)
label.pack()
button.pack()

root.mainloop()