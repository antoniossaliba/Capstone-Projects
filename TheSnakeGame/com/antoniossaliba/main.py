from turtle import Turtle, Screen
import random as rnd

screen = Screen()
screen.title("Snake Game")
screen.setup(900, 900)
screen.bgcolor("black")
screen.listen()

the_snake = Turtle("square")
the_snake.hideturtle()
the_snake.color("green")
the_snake.penup()
the_snake.setposition(-400, 400)
the_snake.showturtle()

the_writer = Turtle()
the_writer.color("white")
the_writer.hideturtle()
the_writer.penup()
the_writer.goto(-390, 430)

def up():
    the_snake.setheading(90)

def down():
    the_snake.setheading(270)

def forward():
    the_snake.setheading(0)

def backward():
    the_snake.setheading(180)

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(forward, "Right")
screen.onkey(backward, "Left")

the_game_is_over = False
score = 0

while not the_game_is_over:

    random_x_cor = rnd.randint(-440, 440)
    random_y_cor = rnd.randint(-430, 430)

    the_dot = Turtle("circle")
    the_dot.hideturtle()
    the_dot.color("red")
    the_dot.penup()
    the_dot.shapesize(1, 1, 1)
    the_dot.setposition(random_x_cor, random_y_cor)
    print(the_dot.xcor(), the_dot.ycor())
    the_dot.showturtle()

    while abs(the_dot.xcor() - int(the_snake.xcor())) > 10 or abs(the_dot.ycor() - int(the_snake.ycor())) > 10:
        the_snake.forward(5)
        if int(the_snake.xcor()) == -450 or int(the_snake.xcor()) == 450 or int(the_snake.ycor()) == -450 or int(the_snake.ycor()) == 450:
            the_snake.hideturtle()
            the_dot.hideturtle()
            the_snake.color("white")
            the_snake.goto(0, 0)
            the_snake.write(f"Game Over!\nYour score: {score}", align="center", font=("Arial", 24, "bold"))
            the_game_is_over = True
            break
        if abs(the_dot.xcor() - int(the_snake.xcor())) <= 10 and abs(the_dot.ycor() - int(the_snake.ycor())) <= 10:
            score += 1
            the_dot.hideturtle()
            break

screen.exitonclick()