from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 425)
        self.score_board(0)

    def score_board(self, increment_score):
        self.score += increment_score
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=("Arial", 20, "normal"))
