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

    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def go_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
