# Simple program demonstrating destroy() functionality
from tkinter import Button, Tk, Label

root = Tk()
labels = []

def create_label():
    label = Label(root, text="I am a label")
    label.pack()
    labels.append(label)

def delete_labels():
    if len(labels) > 0:
        label = labels.pop()
        label.destroy()

add_button = Button(root, text="Add label", command=create_label)
remove_button = Button(root, text="Remove label", command=delete_labels)
add_button.pack()
remove_button.pack()

root.mainloop()

