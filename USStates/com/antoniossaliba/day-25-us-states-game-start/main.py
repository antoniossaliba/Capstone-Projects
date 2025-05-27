from turtle import Screen
from scoreclass import Score
from stateclass import State

screen = Screen()
screen.title("US States Quiz")
screen.bgpic("blank_states_img.gif")
screen.setup(725, 491)

scorer = Score()
state = State()

users_input = screen.textinput(f"{scorer.score}/50 States Correct", "What's another state name?").title()

while users_input not in state.states_list and users_input != "exit".title():
    users_input = screen.textinput(f"{scorer.score}/50 States Correct", "What's another state name?").title()

while len(state.states_list) > 0 and users_input != "exit".title():

    state.create_the_state(users_input)
    scorer.increment_score()
    state.states_list.remove(users_input)

    if len(state.states_list) == 0:
        break

    users_input = screen.textinput(f"{scorer.score}/50 States Correct", "What's another state name?").title()

    while users_input not in state.states_list and users_input != "exit".title():
        users_input = screen.textinput(f"{scorer.score}/50 States Correct", "What's another state name?").title()

state.write_to_csv()

screen.exitonclick()