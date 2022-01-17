from turtle import Turtle
import random


class CreateBlock:
    def __init__(self):
        super().__init__()
        self.segments = []
        self.car()

    def car(self):
        for segment in range(0, random.randint(1, 5)):
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            yaxis = random.randint(-380, 380)
            segment.goto(580, yaxis)
            self.segments.append(segment)
