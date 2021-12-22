# import turtle library
from turtle import Turtle, Screen

# turtle object and set the shape and color
lucy = Turtle()
screen = Screen()
screen.bgcolor("orange")
lucy.shape("turtle")
lucy.color("black")


def draw_dashed_line():
    i = 0
    while i != 10:
        lucy.forward(10)
        lucy.penup()
        lucy.forward(10)
        lucy.pendown()
        i += 1


draw_dashed_line()
screen.exitonclick()
