from turtle import Turtle

class Padel(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.setheading(90)
        self.penup()
        self.color("green")
        self.shapesize(0.2, 3)
        self.goto(350, 0)
        self.showturtle()

    def up(self):
        if self.ycor() <= 253:
            self.setheading(90)
            self.forward(40)


    def down(self):
        if self.ycor() >= -250:
            self.setheading(270)
            self.forward(40)