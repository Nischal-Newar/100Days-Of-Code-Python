# import turtle library
from turtle import Turtle, Screen
import random

# turtle object and set the shape and color
lucy = Turtle()
screen = Screen()
screen.bgcolor("black")
lucy.shape("turtle")
lucy.pensize(10)
lucy.speed("fast")

turtle_movement = ["left", "right"]
turtle_color = ["#78ABC5", "#9AF6ED", "#EBCCA6", "#D24D4D", "#51767F", "#A7F6F6", "#75C3CF", "#579D9D"]

for _ in range(200):
    lucy.color(random.choice(turtle_color))
    lucy.forward(50)
    if random.choice(turtle_movement) == 'left':
        lucy.left(90)
    else:
        lucy.right(90)

screen.exitonclick()
