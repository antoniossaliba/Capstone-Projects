from turtle import Turtle

class LevelCounter(Turtle):

    def __init__(self):
        super().__init__()
        self.speeds = {
            1: 5,
            2: 7,
            3: 10,
            4: 15,
            5: 20
        }
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-210, 280)

    def write_level(self):
        self.clear()
        self.write(f"Current level: {self.level}", align="center", font=("Courier", 12, "bold"))

    def increment_level(self):
        self.level += 1