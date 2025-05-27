from turtle import Turtle
import pandas as pd

class State(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.data_frame = pd.read_csv("50_states.csv")
        self.states_list = self.data_frame["state"].to_list()

    def create_the_state(self, the_state):
        self.color("black")
        self.penup()
        x = self.data_frame[self.data_frame["state"] == the_state]["x"]
        y = self.data_frame[self.data_frame["state"] == the_state]["y"]
        self.goto(x.max(), y.max())
        self.write(the_state, align="center", font=("Courier", 8, "normal"))

    def write_to_csv(self):
        missed_state = []
        x = []
        y = []
        for state in self.states_list:
            missed_state.append(state)
            x.append(self.data_frame[self.data_frame["state"] == state]["x"].max())
            y.append(self.data_frame[self.data_frame["state"] == state]["y"].max())
        data_dict = {
            "state": missed_state,
            "x": x,
            "y": y
        }
        new_data_frame = pd.DataFrame(data_dict)
        new_data_frame.to_csv("missed_states.csv", index=False)