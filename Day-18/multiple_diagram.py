# import turtle library
from turtle import Turtle, Screen

# turtle object and set the shape and color
lucy = Turtle()
screen = Screen()
screen.bgcolor("black")
lucy.shape("turtle")

# different colors
diagram_color = ["#78ABC5", "#9AF6ED", "#EBCCA6", "#D24D4D", "#51767F", "#A7F6F6", "#75C3CF", "#579D9D"]
diagram_color_length = 0


# function to draw the shape
def draw_shape(number_of_sides, color):
    for length in range(number_of_sides):
        interior_angle = 360 / number_of_sides
        lucy.color(color)
        lucy.forward(100)
        lucy.right(interior_angle)


# loop to call the shape function and pass the number of sides and color
for shape_sides in range(3, 11):
    draw_shape(shape_sides, diagram_color[diagram_color_length])
    diagram_color_length += 1

screen.exitonclick()
