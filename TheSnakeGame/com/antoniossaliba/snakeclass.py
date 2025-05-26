from turtle import Turtle
class Snake:

    def __init__(self, snakes=list()):
        if snakes is None:
            snakes = list()
        self.snakes = snakes
        self.left_offset = 0
        for _ in range(3):
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("green")
            turtle.setposition(-self.left_offset, 0)
            self.snakes.append(turtle)
            self.left_offset += 20

    def move(self):
        count = len(self.snakes) - 1
        while count >= 1:
            self.snakes[count].setposition((self.snakes[count - 1].xcor(), self.snakes[count - 1].ycor()))
            count -= 1
        self.snakes[count].forward(20)

    def up(self):
        if self.snakes[0].heading() != 270:
            count = len(self.snakes) - 1
            while count >= 1:
                self.snakes[count].setposition((self.snakes[count - 1].xcor(), self.snakes[count - 1].ycor()))
                count -= 1
            self.snakes[count].setheading(90)
        else:
            print("Cannot go up!")

    def down(self):
        if self.snakes[0].heading() != 90:
            count = len(self.snakes) - 1
            while count >= 1:
                self.snakes[count].setposition((self.snakes[count - 1].xcor(), self.snakes[count - 1].ycor()))
                count -= 1
            self.snakes[count].setheading(270)
        else:
            print("Cannot go down!")

    def right(self):
        if self.snakes[0].heading() != 180:
            count = len(self.snakes) - 1
            while count >= 1:
                self.snakes[count].setposition((self.snakes[count - 1].xcor(), self.snakes[count - 1].ycor()))
                count -= 1
            self.snakes[count].setheading(0)
        else:
            print("Cannot go right!")

    def left(self):
        if self.snakes[0].heading() != 0:
            count = len(self.snakes) - 1
            while count >= 1:
                self.snakes[count].setposition((self.snakes[count - 1].xcor(), self.snakes[count - 1].ycor()))
                count -= 1
            self.snakes[count].setheading(180)
        else:
            print("Cannot go left!")

    def the_game_is_over(self):
        writer = Turtle()
        writer.hideturtle()
        writer.color("white")
        writer.penup()
        writer.write("Game Over!", align="center", font=("Courier", 24, "normal"))

    def extend(self):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("green")
        turtle.setposition(self.snakes[len(self.snakes) - 1].xcor() - self.left_offset, self.snakes[len(self.snakes) - 1].ycor())
        self.snakes.append(turtle)

    def check_for_collision(self):
        idx = len(self.snakes) - 1
        while idx >= 1:
            head = self.snakes[0]
            the_tested_part = self.snakes[idx]
            if head.xcor() == the_tested_part.xcor() and head.ycor() == the_tested_part.ycor():
                return True
                break
            idx -= 1
        return False