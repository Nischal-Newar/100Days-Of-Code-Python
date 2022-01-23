# import packages
import time
from turtle import Screen
from create_turtle import CreateTurtle
from create_blocks import CreateBlock

# setup screen
screen = Screen()
screen.tracer(0)
screen.setup(width=1200, height=800)
screen.colormode(255)
screen.bgcolor("#129793")
screen.title("Turtle Crossing Game")

# create the turtle
lucy = CreateTurtle()
first_car_lane = CreateBlock()
second_car_lane = CreateBlock()

# listen to keystroke
screen.listen()
screen.onkeypress(lucy.turtle_move_forward, 'Up')
screen.onkeypress(lucy.turtle_move_backward, 'Down')

# game loop
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    # generate car and move it backwards
    first_car_lane.car(580, 20, 321)
    second_car_lane.car(-580, -321, -20)
    first_car_lane.car_move('backward')
    second_car_lane.car_move('forward')

    for car in first_car_lane.all_blocks:
        if car.distance(lucy) < 30:
            is_game_on = False

    for car in second_car_lane.all_blocks:
        if car.distance(lucy) < 30:
            is_game_on = False

# close the screen on click
screen.exitonclick()
