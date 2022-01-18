from turtle import Turtle
import random

# global values
CAR_COLOR_SCHEME = ['#F25E74', '#FF8884', '#026178', '#0682A6', '#34A1C7']
STARTING_MOVE_DISTANCE = 5


class CreateBlock:
    def __init__(self):
        self.all_blocks = []

    def car(self):
        random_car_spawn = random.randint(1, 6)
        if random_car_spawn == 1:
            car = Turtle('square')
            car.color(random.choice(CAR_COLOR_SCHEME))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            yaxis = random.randint(-300, 300)
            car.goto(580, yaxis)
            self.all_blocks.append(car)

    def car_move(self):
        for car in self.all_blocks:
            car.backward(STARTING_MOVE_DISTANCE)
