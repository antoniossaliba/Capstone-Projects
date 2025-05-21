from art import art2
import random as rnd

print(art2)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
the_random_number = rnd.randint(0, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number_of_guesses = 0

while difficulty != "easy" and difficulty != "hard":
    print("You have to input 'easy' or 'hard'.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    number_of_guesses = 10
else:
    number_of_guesses = 5

found_the_result = False

while number_of_guesses > 0 and not found_the_result:

    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
    the_guess = int(input("Make a guess: "))

    if the_guess < the_random_number:
        print("Too low.")
    elif the_guess > the_random_number:
        print("Too high.")
    else:
        print(f"Congratulations! You guess it! The number was {the_random_number}.")
        found_the_result = True
        continue

    print("Guess again.")
    number_of_guesses -= 1

if number_of_guesses == 0:
    print("You ran out of lives you can't guess anymore!")
