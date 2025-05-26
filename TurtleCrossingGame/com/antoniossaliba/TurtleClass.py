from turtle import Turtle

class TurtleCrosser(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.hideturtle()
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.showturtle()

    def up(self):
        self.forward(10)

    def does_turtle_crossed(self):
        return int(self.ycor()) > 280