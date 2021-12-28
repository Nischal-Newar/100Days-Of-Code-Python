# import libraries
from turtle import Turtle

# constant global variables
INITIAL_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_MOVEMENT_SPEED = 20


class SnakeBody:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            new_snake_segment = Turtle("square")
            new_snake_segment.color("white")
            new_snake_segment.penup()
            self.segments.append(new_snake_segment)

    def snake_movement(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x_cords = self.segments[segment - 1].xcor()
            new_y_cords = self.segments[segment - 1].ycor()
            self.segments[segment].setposition(new_x_cords, new_y_cords)
        self.segments[0].forward(FORWARD_MOVEMENT_SPEED)

