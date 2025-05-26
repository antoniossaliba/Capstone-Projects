from turtle import Turtle

class GameOverWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")

    def write_game_over(self):
        self.clear()
        self.write("Game Over!", align="center", font=("Courier", 24, "bold"))

    def write_you_won(self):
        self.clear()
        self.write("You won!", align="center", font=("Courier", 24, "bold"))