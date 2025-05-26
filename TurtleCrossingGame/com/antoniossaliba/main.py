from turtle import Screen
from TurtleClass import TurtleCrosser
from LevelCounterClass import LevelCounter
from CarClass import Car
from GameOverWriterClass import GameOverWriter
import time

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

turtle = TurtleCrosser()
level_counter = LevelCounter()
game_over_writer = GameOverWriter()
cars_list = []

screen.onkeypress(turtle.up, "Up")

game_is_on = True

while level_counter.level != 6 and game_is_on:
    time.sleep(0.1)
    car = Car()
    cars_list.append(car)
    level_counter.write_level()
    screen.update()

    if not turtle.does_turtle_crossed():
        for car in cars_list:
            if car.distance(turtle) < 20:
                game_is_on = False
                game_over_writer.write_game_over()
                break
            car.forward(level_counter.speeds[level_counter.level])
    else:
        level_counter.increment_level()
        turtle.goto(0, -280)

if level_counter.level == 6:
    game_over_writer.write_you_won()

screen.exitonclick()