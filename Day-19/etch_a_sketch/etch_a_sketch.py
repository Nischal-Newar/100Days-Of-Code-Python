# import modules
from turtle import Screen, Turtle

# setup turtle
lucy = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("#4D7F7B")
lucy.shape("arrow")
lucy.speed("fast")


def move_forward():
    lucy.forward(10)


def move_backward():
    lucy.back(10)


def move_left():
    lucy.left(10)


def move_right():
    lucy.right(10)


def clear_screen():
    lucy.penup()
    lucy.clear()
    lucy.home()
    lucy.pendown()


# listen to the keyboard strokes
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")
screen.onkeypress(clear_screen, "c")

screen.exitonclick()
