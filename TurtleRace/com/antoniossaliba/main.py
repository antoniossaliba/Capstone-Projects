from turtle import Turtle, Screen
import random as rnd

screen = Screen()
screen.setup(500, 400)
user_input = screen.textinput("Make your bet", "Which turtle will win the race? Input the color").lower()

while user_input != "red" and user_input != "blue" and user_input != "green" and user_input != "yellow" and user_input != "orange" and user_input != "purple":
    user_input = screen.textinput("Make your bet", "Which turtle will win the race? Input the color").lower()

colors = ["red", "blue", "green", "yellow", "orange", "purple"]

# turtle1 = Turtle("turtle")
# turtle1.penup()
# turtle1.color(colors[0])
# turtle1.goto(-230, -100)
# turtle2 = Turtle("turtle")
# turtle2.penup()
# turtle2.color(colors[1])
# turtle2.goto(-230, -50)
# turtle3 = Turtle("turtle")
# turtle3.penup()
# turtle3.color(colors[2])
# turtle3.goto(-230, 0)
# turtle4 = Turtle("turtle")
# turtle4.penup()
# turtle4.color(colors[3])
# turtle4.goto(-230, 50)
# turtle5 = Turtle("turtle")
# turtle5.penup()
# turtle5.color(colors[4])
# turtle5.goto(-230, 100)
# turtle6 = Turtle("turtle")
# turtle6.penup()
# turtle6.color(colors[5])
# turtle6.goto(-230, 150)

y_coordinate = -100
turtles = []
for color in colors:
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(-230, y_coordinate)
    turtles.append(turtle)
    y_coordinate += 50

race_is_off = False
the_winner_turtle = turtles[0]

while not race_is_off:
    for turtle in turtles:
        random_step = rnd.randint(0, 10)
        turtle.forward(random_step)
        if int(turtle.xcor()) >= 240:
            race_is_off = True
            the_winner_turtle = turtle
            break

if the_winner_turtle.color()[0] == user_input:
    screen.clear()
    screen.bgcolor("green")
else:
    screen.clear()
    screen.bgcolor("red")

screen.exitonclick()