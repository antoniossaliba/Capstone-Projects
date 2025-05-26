from turtle import Turtle

class Player2Padel(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.shape("square")
        self.penup()
        self.goto(-350, 0)
        self.setheading(90)
        self.shapesize(0.2, 3)
        self.showturtle()

    def up(self):
        if self.ycor() <= 253:
            self.setheading(90)
            self.forward(40)


    def down(self):
        if self.ycor() >= -250:
            self.setheading(270)
            self.forward(40)