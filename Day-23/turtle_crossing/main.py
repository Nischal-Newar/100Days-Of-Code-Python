from turtle import Screen
from create_turtle import CreateTurtle
from create_blocks import CreateBlock
import random

# setup screen
screen = Screen()
screen.tracer(0)
screen.setup(width=1200, height=800)
screen.colormode(255)
screen.bgcolor("#129793")
screen.title("Turtle Crossing Game")

# create the turtle
lucy = CreateTurtle()

# listen to keystroke
screen.listen()
screen.onkeypress(lucy.turtle_move_forward, 'Up')
screen.onkeypress(lucy.turtle_move_backward, 'Down')

# game loop
for rando in range(1, random.randint(1, 10)):
    rando = CreateBlock()
is_game_on = True
while is_game_on:
    screen.update()

# close the screen on click
screen.exitonclick()
