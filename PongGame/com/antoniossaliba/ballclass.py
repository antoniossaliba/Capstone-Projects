from turtle import Turtle
import random as rnd

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.setheading(rnd.randint(-45, 45))

    def move(self):
        if int(self.ycor()) > 280 or int(self.ycor()) < -280:
            self.setheading(-self.heading())
        self.forward(20)

    def check_for_bounds(self):
        return int(self.xcor()) < 370 and int(self.xcor()) > -370