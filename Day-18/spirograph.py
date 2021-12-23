# import turtle library
from turtle import Turtle, Screen
import random

# turtle object and set the shape and color
lucy = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("#4D7F7B")
lucy.shape("turtle")
lucy.speed("fastest")


# random color generator
def random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return red, green, blue


# for loop to create the spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        # random color selection
        lucy.color(random_color())
        lucy.circle(100)
        lucy.right(size_of_gap)


draw_spirograph(10)
screen.exitonclick()
