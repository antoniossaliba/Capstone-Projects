from turtle import Screen
from player2padelclass import Player2Padel
from padelclass import Padel
from scoreboard import ScoreBoard
from ballclass import Ball
import time

screen = Screen()
screen.tracer(0)
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

padel1 = Padel()
padel2 = Player2Padel()
score_board = ScoreBoard()

screen.listen()
screen.onkeypress(padel1.up, "Up")
screen.onkeypress(padel1.down, "Down")
screen.onkeypress(padel2.up, "w")
screen.onkeypress(padel2.down, "s")

ball = Ball()

while score_board.score_of_player1 != 5 and score_board.score_of_player2 != 5:

    time.sleep(0.1)
    score_board.write_score_of_players()
    ball.move()
    screen.update()

    if ball.distance(padel1) < 50 and ball.xcor() > 330:
        ball.hideturtle()
        ball.setheading(ball.heading() - 90)
        ball.showturtle()
    if ball.distance(padel2) < 50 and ball.xcor() < -330:
        ball.hideturtle()
        ball.setheading(ball.heading() - 90)
        ball.showturtle()

    if not ball.check_for_bounds():
        if ball.xcor() > 360:
            score_board.increment_score1()
        else:
            score_board.increment_score2()
        ball.hideturtle()
        ball = Ball()


screen.reset()
score_board.state_winner()


screen.exitonclick()