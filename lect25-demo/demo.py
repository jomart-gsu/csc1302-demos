"""
Incomplete Pong game demo. You're invited to try to get the game fully working!
"""
from tkinter import Tk, Canvas

root = Tk()

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

ball = canvas.create_oval(
    CANVAS_WIDTH / 2 - 10,
    CANVAS_HEIGHT / 2 - 10,
    CANVAS_WIDTH / 2 + 10,
    CANVAS_HEIGHT / 2 + 10,
    fill='red'
)
paddle = canvas.create_rectangle(
    CANVAS_WIDTH / 2 - PADDLE_WIDTH / 2,
    CANVAS_HEIGHT - PADDLE_HEIGHT,
    CANVAS_WIDTH / 2 + PADDLE_WIDTH / 2,
    CANVAS_HEIGHT,
    fill="blue"
)
x_direction = 0
y_direction = 1
is_started = False

def move_ball():
    global y_direction, x_direction
    if canvas.coords(ball)[3] == CANVAS_HEIGHT:
        y_direction = -1
    if canvas.coords(ball)[1] == 0:
        y_direction = 1
    if canvas.coords(ball)[2] >= CANVAS_WIDTH:
        x_direction *= -1
    if canvas.coords(ball)[0] <= 0:
        x_direction *= -1

    canvas.move(ball, x_direction, y_direction)
    root.after(10, move_ball)

def move_paddle_left(event):
    canvas.move(paddle, -5, 0)

def move_paddle_right(event):
    canvas.move(paddle, 5, 0)

def start_animation(event):
    global is_started
    if not is_started:
        root.after(10, move_ball)
        is_started = True

root.bind("<Button>", start_animation)
root.bind("<Left>", move_paddle_left)
root.bind("<Right>", move_paddle_right)
root.mainloop()