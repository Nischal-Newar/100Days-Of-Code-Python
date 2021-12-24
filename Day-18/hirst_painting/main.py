# import libraries
import colorgram
from turtle import Turtle, Screen
import random

# extract the colors from the image and create a color palette
colors = colorgram.extract("./hirst_painting.jpg", 15)
color_palette = []
for color in colors:
    color_palette.append((color.rgb.r, color.rgb.g, color.rgb.b))

# turtle object and set the shape and color
lucy = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("#4D7F7B")
lucy.shape("turtle")
lucy.penup()
lucy.hideturtle()
lucy.setposition(-200, 200)
lucy.speed("fastest")

# 10x10 dot painting
for row in range(1, 101):
    lucy.dot(15, random.choice(color_palette))
    lucy.forward(50)
    # if even row take a 180 on left side
    if row % 20 == 0:
        lucy.left(90)
        lucy.forward(50)
        lucy.left(90)
        lucy.forward(50)
    # if odd row take a 180 on right side
    elif row % 10 == 0:
        lucy.right(90)
        lucy.forward(50)
        lucy.right(90)
        lucy.forward(50)

screen.exitonclick()
