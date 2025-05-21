from art import art3
import random as rnd
from data import celebrities
from art import art4

rnd_a = rnd.randint(0, len(celebrities) - 1)
rnd_b = rnd.randint(0, len(celebrities) - 1)

A = {}
B = {}

count_a = -1
count_b = -1

for key in celebrities:
    if count_a == rnd_a - 1:
        A = celebrities[key]
        break
    count_a += 1

for key in celebrities:
    if count_b == rnd_b - 1:
        B = celebrities[key]
        break
    count_b += 1

my_score = 0

answer_is_true = False

print(art3)

print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")

print(art4)

print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

the_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

while the_answer != "a" and the_answer != "b":
    print("You have to input 'A' or 'B'. Please try again.")
    the_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

if the_answer == "a":
    if A["followers"] > B["followers"]:
        answer_is_true = True
        my_score += 1
    elif A["followers"] < B["followers"]:
        answer_is_true = False
    else:
        answer_is_true = True
        print("Draw!")

else:
    if A["followers"] < B["followers"]:
        answer_is_true = True
        my_score += 1
        A = B
    elif A["followers"] > B["followers"]:
        answer_is_true = False
    else:
        answer_is_true = True
        print("Draw!")

while answer_is_true:
    print("\n" * 100)
    print(art3)
    print(f"You're right! Current score: {my_score}.")
    B = {}
    rnd_b = rnd.randint(0, len(celebrities) - 1)
    count_b = -1
    for key in celebrities:
        if count_b == rnd_b - 1:
            B = celebrities[key]
            break
        count_b += 1
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(art4)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

    the_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    while the_answer != "a" and the_answer != "b":
        print("You have to input 'A' or 'B'. Please try again.")
        the_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if the_answer == "a":
        if A["followers"] > B["followers"]:
            answer_is_true = True
            my_score += 1
        elif A["followers"] < B["followers"]:
            answer_is_true = False
        else:
            answer_is_true = True
            print("Draw!")

    else:
        if A["followers"] < B["followers"]:
            answer_is_true = True
            my_score += 1
            A = B
        elif A["followers"] > B["followers"]:
            answer_is_true = False
        else:
            answer_is_true = True
            print("Draw!")

print("\n" * 100)
print(art3)
print(f"Sorry, that's wrong. Final score: {my_score}")
