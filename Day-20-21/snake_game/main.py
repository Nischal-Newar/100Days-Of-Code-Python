# import libraries
import time
from turtle import Screen
from snake import SnakeBody
from food import Food
from score import Score

# setup screen and betting input
screen = Screen()
screen.setup(width=900, height=900)
screen.colormode(255)
screen.tracer(0)
screen.bgcolor("black")

# create the snake body
snake = SnakeBody()
screen.update()

# create food
food = Food()

# create scoreboard
score = Score()

# listen to keystroke
screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")


# snake movement
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.snake_movement()

    # detect collision with food
    if snake.head.distance(food) < 15:
        score.score_board(1)
        food.change_location()

    # detect collision with walls
    if snake.head.xcor() > 440 or snake.head.ycor() > 440 or snake.head.xcor() < -440 or snake.head.ycor() < -440:
        is_game_on = False
        score.game_over()

screen.exitonclick()
