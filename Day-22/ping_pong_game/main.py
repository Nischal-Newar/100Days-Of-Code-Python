from turtle import Screen
from paddle import Paddle

# global values
PADDLE_LOCATION = [(430, 0), (-435, 0)]

# setup screen
screen = Screen()
screen.tracer(0)
screen.setup(width=900, height=900)
screen.colormode(255)
screen.bgcolor("#129793")
screen.title("Snake Game")

# create paddles
first_paddle = Paddle(PADDLE_LOCATION[0])
second_paddle = Paddle(PADDLE_LOCATION[1])
screen.update()





# listen to keystroke
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_up, "s")


# exit the screen on click after the game ends
screen.exitonclick()
