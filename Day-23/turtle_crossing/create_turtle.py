from turtle import Turtle


class CreateTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("White")
        self.penup()
        self.goto(0, -380)
        self.setheading(90)

    def turtle_move_forward(self):
        new_yaxis = self.ycor() + 10
        self.goto(0, new_yaxis)

    def turtle_move_backward(self):
        if self.ycor() != -380:
            new_yaxis = self.ycor() - 10
            self.goto(0, new_yaxis)
