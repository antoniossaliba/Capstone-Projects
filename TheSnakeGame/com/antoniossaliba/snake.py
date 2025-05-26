from turtle import Screen
from snakeclass import Snake
from foodclass import Food
from scoreclass import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

score = Score()

food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.write_score()

    if snake.snakes[0].xcor() > 300 or snake.snakes[0].xcor() < -300 or snake.snakes[0].ycor() > 300 or snake.snakes[0].ycor() < -300 or snake.check_for_collision():
        snake.the_game_is_over()
        game_is_on = False
        continue

    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        score.increment_score()
        snake.extend()

screen.exitonclick()