from turtle import Turtle
import random as rnd

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.colors_list = ["red", "blue", "pink", "yellow", "orange", "green"]
        self.hideturtle()
        self.color(self.colors_list[rnd.randint(0, len(self.colors_list) - 1)])
        self.penup()
        random_y = rnd.randint(-260, 260)
        self.goto(300, random_y)
        self.shape("square")
        self.shapesize(0.5, 1)
        self.setheading(180)
        self.showturtle()
        self.car_speed = 10