from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# global values
PADDLE_LOCATION = [(580, 0), (-590, 0)]

# setup screen
screen = Screen()
screen.tracer(0)
screen.setup(width=1200, height=800)
screen.colormode(255)
screen.bgcolor("Black")
screen.title("Snake Game")

# create paddles
right_paddle = Paddle(PADDLE_LOCATION[0])
left_paddle = Paddle(PADDLE_LOCATION[1])

# create scoreboard
score = Scoreboard()

# listen to keystroke
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

# create ball
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    # detect collision with the top and bottom wall and change the ball direction
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_yaxis()

    # detect collision with paddle and change the ball direction
    if ball.xcor() > 550 and ball.distance(right_paddle) < 50 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -560:
        ball.bounce_xaxis()

    # detect if left paddle misses
    if ball.xcor() < -580:
        ball.reset_position()
        score.right_point()

    # detect if right paddle misses
    if ball.xcor() > 580:
        ball.reset_position()
        score.left_point()

# exit the screen on click after the game ends
screen.exitonclick()
