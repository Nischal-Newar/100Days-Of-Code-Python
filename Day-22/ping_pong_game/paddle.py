from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("#005B9A")
        self.speed("fastest")
        self.goto(location)

    def go_up():
        y_cor = first_paddle.ycor() + 20
        first_paddle.goto(first_paddle.xcor(), y_cor)
        screen.update()

    def go_down():
        y_cor = first_paddle.ycor() - 20
        first_paddle.goto(first_paddle.xcor(), y_cor)
        screen.update()