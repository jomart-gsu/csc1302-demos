from tkinter import Tk, Canvas

root = Tk()
canvas = Canvas(root, width=200, height=200)
canvas.pack()
# upper-left corner, lower-right corner
ball = canvas.create_oval(90, 90, 110, 110, fill='red')
direction = "down"

def move_ball():
    global ball, direction
    if direction == "down":
        if canvas.coords(ball)[3] == 200:
            direction = "up"
    elif direction == "up":
        if canvas.coords(ball)[1] == 0:
            direction = "down"

    canvas.move(ball, 0, 1 if direction == "down" else -1)
    root.after(10, move_ball)

move_ball()
root.mainloop()


# root.bind("<Left>", left_stuff)
# root.bind("<Right>", right_stuff)