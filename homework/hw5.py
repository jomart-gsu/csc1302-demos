from tkinter import Tk, Button, Label, Entry, StringVar, Frame, Text, messagebox


class LinkedListGUINode:
    def __init__(self, value, next=None):
        self.value = value
        self.widget = Label(game_frame, text=f"{value}")
        self.widget.pack()
        self.next = next


class PotatoGame:
    def __init__(self):
        pass

    def setup(self, n, k):
        self.k = k
        self.head = LinkedListGUINode(0)
        cur = self.head
        for i in range(1, n):
            cur.next = LinkedListGUINode(i)
            cur = cur.next

        cur.next = self.head  # finish the circle
        self.cur = self.head  # need to track where we are in the game

    def step(self):
        for _ in range(self.k-2):
            self.cur = self.cur.next

        t.insert('end', f"{self.cur.next.value} is eliminated.\n")

        # we've taken k-1 steps, so delete the NEXT node
        self.cur.next.widget.destroy()
        self.cur.next = self.cur.next.next

        # start the next round from the node after the removed one
        self.cur = self.cur.next

        if self.cur.next == self.cur:
            self.cur.widget.destroy()
            messagebox.showinfo(message=f"Player {self.cur.value} won!")
            t.delete(1.0, 'end')  # clear the text widget, per https://stackoverflow.com/questions/27966626/how-to-clear-delete-the-contents-of-a-tkinter-text-widget
            reset()


def start_game():
    n = int(n_var.get())
    k = int(k_var.get())
    if n < 2 or n > 12:
        messagebox.showinfo(message="N must be between 2 and 12")
    if k < 1:
        messagebox.showinfo(message="K must be greater than 1")

    game.setup(n, k)
    eliminate_button.pack()
    start_button.pack_forget()


def eliminate():
    game.step()


def reset():
    eliminate_button.pack_forget()
    start_button.pack()
    # clear the text entries (I had to look up how to do this, not required)
    n_var.set("")
    k_var.set("")


root = Tk()
game = PotatoGame()

n_var = StringVar()
k_var = StringVar()
control_frame = Frame(root, width=100, height=100)

n_entry = Entry(control_frame, textvariable=n_var)
k_entry = Entry(control_frame, textvariable=k_var)
n_entry.pack()
k_entry.pack()

start_button = Button(control_frame, text="Start", command=start_game)
eliminate_button = Button(control_frame, text="Eliminate", command=eliminate)
start_button.pack()

control_frame.pack()


game_frame = Frame(root, width=300, height=200)
game_frame.pack()

t = Text(root, width=200)
t.pack()

root.mainloop()