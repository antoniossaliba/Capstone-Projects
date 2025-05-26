from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        self.score_of_player1 = 0
        self.score_of_player2 = 0
        super().__init__()
        self.pensize(10)
        self.penup()
        self.hideturtle()


    def write_score_of_players(self):
        self.penup()
        self.hideturtle()
        self.goto(-50, 270)
        self.color("red")
        self.clear()
        self.write(self.score_of_player1, align="center", font=("Courier", 20, "bold"))

        self.penup()
        self.hideturtle()
        self.goto(0, 290)
        self.setheading(270)
        self.color("white")
        y_coordinate = self.ycor()
        while y_coordinate >= -280:
            if self.isdown():
                self.penup()
            else:
                self.pendown()
            self.forward(10)
            y_coordinate = self.ycor()

        self.penup()
        self.hideturtle()
        self.goto(50, 270)
        self.color("green")
        self.write(self.score_of_player2, align="center", font=("Courier", 20, "bold"))

    def increment_score1(self):
        self.score_of_player1 += 1

    def increment_score2(self):
        self.score_of_player2 += 1

    def state_winner(self):
        self.home()
        if self.score_of_player1 == 5:
            self.color("red")
            self.write("Player 2 won!", align="center", font=("Courier", 24, "bold"))
        else:
            self.color("green")
            self.write("Player 1 won!", align="center", font=("Courier", 24, "bold"))