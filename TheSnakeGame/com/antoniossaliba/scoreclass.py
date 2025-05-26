from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0

    def increment_score(self):
        self.score += 1

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))
