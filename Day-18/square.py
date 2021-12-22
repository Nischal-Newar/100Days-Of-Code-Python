# import turtle library
from turtle import Turtle, Screen

lucy = Turtle()
lucy.shape("turtle")
lucy.color("black")

i = 0
while i != 4:
    lucy.forward(100)
    lucy.right(90)
    i += 1

lucy.Screen()
