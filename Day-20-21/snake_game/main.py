# import libraries
import time
from turtle import Screen
from snake import SnakeBody

# setup screen and betting input
screen = Screen()
screen.setup(width=900, height=900)
screen.colormode(255)
screen.tracer(0)
screen.bgcolor("black")

# create the snake body
snake = SnakeBody()
screen.update()

# snake movement
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.snake_movement()

screen.exitonclick()
