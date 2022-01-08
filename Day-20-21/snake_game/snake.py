# import libraries
from turtle import Turtle

# constant global variables
INITIAL_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_MOVEMENT_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_COLOR = ['#005B9A', "#FF7260", '#6C2D58']
SNAKE_PATTERN_COLOR = 3


class SnakeBody:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in INITIAL_COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        if position == (0, 0):
            new_snake_segment = Turtle("circle")
            new_snake_segment.shapesize(1, 2)
            new_snake_segment.color(SNAKE_COLOR[0])
        elif len(self.segments) % 3 == 0:
            new_snake_segment = Turtle("square")
            new_snake_segment.color(SNAKE_COLOR[1])
        else:
            new_snake_segment = Turtle("square")
            new_snake_segment.color(SNAKE_COLOR[2])
        new_snake_segment.penup()
        new_snake_segment.goto(position)
        self.segments.append(new_snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def snake_movement(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x_cords = self.segments[segment - 1].xcor()
            new_y_cords = self.segments[segment - 1].ycor()
            self.segments[segment].setposition(new_x_cords, new_y_cords)
        self.segments[0].forward(FORWARD_MOVEMENT_SPEED)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
