# print("Welcome to the Band Name Generator.")
# city = input("What's the name of the city you grew up in?\n")
# pet = input("What's your pet's name?\n")
# print("Your band name could be", city, pet)
#import random
# print(type(123))
# print(type(""))
# print(type(3.14))
# print(type(True))

# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# print(7 // 2)
# print(7 / 2)

# print(5**2)

# print(3 * (3 + 3) / 3 - 3)

# print(round(31.7))
# print(round(31.4))

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# print(f"Each person should pay: ${round((bill * ((tip / 100) + 1)) / people, 2)}")

# height = int(input("What is your height in cm? "))
# age = int(input("Enter your age: "))
#
# if height > 120:
#      print("Can ride.")
#      if age > 18:
#          print("You have to pay $12.")
#      elif age < 12:
#          print("You have to pay $5.")
#      else:
#          print("You have to pay $7.")
#
# else:
#      print("Can't ride.")

# print(10 % 3)

# number = int(input("Enter a number: "))
#
# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your total bill is ${bill}")

# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************''')
#
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# direction1 = input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\"\n")
#
# if direction1.lower() == "left":
#     direction2 = input("Do you want to swim or wait?\n")
#     if direction2.lower() == "wait":
#         direction3 = input("There is 3 doors in front of you. Which one would you choose? Red, Yellow, or Blue?\n")
#         if direction3.lower() == "yellow":
#             print("You Won!")
#         else:
#             if direction3.lower() == "red":
#                 print("Burned by fire. Game Over!")
#             elif direction3.lower() == "blue":
#                 print("Eaten by beasts. Game Over!")
#             else:
#                 print("Game Over!")
#     else:
#         print("Attacked by trout. Game Over!")
# else:
#     print("Fall into a hole. Game Over!")

# import random as rnd
#
# num = rnd.randint(0, 1)
#
# if num == 0:
#     print("Heads")
# else:
#     print("Tails")

# import random as rnd
#
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#
# num = rnd.randint(0, len(friends) - 1)
#
# print(friends[num])

# import random as rnd
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)'''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)'''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)'''
#
# my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#
# his_choice = rnd.randint(0, 2)
#
# if my_choice == 0:
#     print(rock)
#     print("Computer chose:")
#
#     if his_choice == 0:
#         print(rock)
#         print("It's a draw")
#     elif his_choice == 1:
#         print(paper)
#         print("You lose")
#     else:
#         print(scissors)
#         print("You win!")
#
# elif my_choice == 1:
#     print(paper)
#     print("Computer chose:")
#
#     if his_choice == 0:
#         print(rock)
#         print("You win!")
#     elif his_choice == 1:
#         print(paper)
#         print("It's a draw")
#     else:
#         print(scissors)
#         print("You lose")
#
# elif my_choice == 2:
#     print(scissors)
#     print("Computer chose:")
#
#     if his_choice == 0:
#         print(rock)
#         print("You lose")
#     elif his_choice == 1:
#         print(paper)
#         print("You win!")
#     else:
#         print(scissors)
#         print("It's a draw")
#
# else:
#     print("Invalid choice!")

# fruits = ["Apple", "Peach", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#
# for i in range(len(fruits)):
#     print(fruits[i])

# scores = [101, 102, 98, 1, 132, -32, 5, 201]
#
# print(max(scores))
#
# maximum = scores[0]
#
# for score in scores:
#     if score > maximum:
#         maximum = score
#
# print(maximum)

# import random as rnd
#
# alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# letters = []
#
# for letter in alphabet:
#     letters.append(letter)
#
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
#
# number_of_letters = int(input("How many letters would you like in your password?\n"))
# number_of_symbols = int(input("How many symbols would you like?\n"))
# number_of_numbers = int(input("How many numbers would you like?\n"))
#
# sorted_list = []
#
# for i in range(number_of_letters):
#     sorted_list.append(letters[rnd.randint(0, len(letters) - 1)])
#
# for j in range(number_of_symbols):
#     sorted_list.append(symbols[rnd.randint(0, len(symbols) - 1)])
#
# for k in range(number_of_numbers):
#     sorted_list.append(numbers[rnd.randint(0, len(numbers) - 1)])
#
# print(sorted_list)
# random.shuffle(sorted_list)
# print(sorted_list)
#
# final_password = ""
#
# for letter in sorted_list:
#     final_password += letter
#
# print(f"Your password is: {final_password}")

# import random as rnd
#
# word_list = ["aardvark", "baboon", "camel"]
#
# lives = 6
#
# chosen_word = word_list[rnd.randint(0, len(word_list) - 1)]
#
# print(chosen_word)
#
# placeholder = ""
#
# for i in range(len(chosen_word)):
#     placeholder += "_"
#
# print(placeholder)
#
# guessed_letters = []
#
# while "_" in placeholder and lives > 0:
#
#     guess = input("Guess a letter: ").lower()[0:1]
#
#     if guess in guessed_letters:
#         print(f"You already guessed {guess}.")
#         print(placeholder)
#         continue
#     else:
#         guessed_letters.append(guess)
#
#     if guess not in chosen_word:
#         lives -= 1
#         print(f"{guess} is not in the chosen word, {lives} lives left!")
#         print(placeholder)
#         continue
#
#     for i in range(len(chosen_word)):
#         if guess == chosen_word[i]:
#             placeholder = placeholder[0:i] + guess + placeholder[i+1:]
#
#     print(placeholder)
#
# if lives == 0:
#     print("You lose!")
# else:
#     print("You guessed it!")

# def greet():
#     print("Hello")
#     print("My name is:")
#     print("Antonios Saliba")
#
# greet()

# def greet_with_name(name):
#     print("Hello", name)
#
# greet_with_name("Antonios")

# letters = 'abcdefghijklmnopqrstuvwxyz'
#
# alphabet = []
#
# for letter in letters:
#     alphabet.append(letter)
#
#
# def encrypt(original_text, shift_amount):
#     original_text_modified = ""
#     for letter in original_text:
#         if letter in alphabet:
#             original_text_modified += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
#         else:
#             original_text_modified += letter
#     return original_text_modified
#
# def decrypt(original_text, shift_amount):
#     original_text_modified = ""
#     for letter in original_text:
#         if letter in alphabet:
#             original_text_modified += alphabet[(alphabet.index(letter) - shift_amount) % len(alphabet)]
#         else:
#             original_text_modified += letter
#     return original_text_modified
#
# print('''
# ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
# a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8
# 8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88''')
#
# print('''
#             88             88
#            ""             88
#                           88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
# 8b         88 88       d8 88       88 8PP""""""" 88
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
#  '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88
#               88
#               88           ''')
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# message = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# if direction == 'encode':
#     print(f"Here's the encoded result: {encrypt(message, shift)}")
# else:
#     print(f"Here's the decoded result: {decrypt(message, shift)}")
#
# confirmation = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
#
# while confirmation == "yes":
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     message = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#
#     if direction == "encode":
#         print(f"Here's the encoded result: {encrypt(message, shift)}")
#     else:
#         print(f"Here's the decoded result: {decrypt(message, shift)}")
#
#     confirmation = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
#
# print("Goodbye")

# my_dict = dict()
#
# name = input("What is your name?: ")
# bid = int(input("What is your bid?: $"))
#
# my_dict[name] = bid
#
# confirmation = input("Are there any other bidders? Type \'yes\' or \'no\'.\n").lower()
#
# while confirmation == "yes":
#     print("\n" * 100)
#     name = input("What is your name?: ")
#     bid = int(input("What is your bid?: $"))
#
#     my_dict[name] = bid
#
#     confirmation = input("Are there any other bidders? Type \'yes\' or \'no\'.\n").lower()
#
# winner_name = ""
# winner_bid = 0
#
# for key in my_dict:
#     if my_dict[key] > winner_bid:
#         winner_name = key
#         winner_bid = my_dict[key]
#
# print(f"The winner is {winner_name} with a bid of ${winner_bid}")

# def format_name(f_name, l_name):
#     f_name = f_name.capitalize()
#     l_name = l_name.capitalize()
#     return f_name + " " + l_name
#
# print(format_name("antOnios", "SALiba"))
#
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
# operations = {
#
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
#
# }
#
#
# art = '''
#  _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
# |_____________________|'''
#
# while True:
#
#     print(art)
#
#     first_number = float(input("What's the first number?: "))
#
#     for key in operations:
#         print(key)
#
#     operation = input("Pick an operation: ")
#
#     second_number = float(input("What's the next number?: "))
#
#     print(f"{first_number} {operation} {second_number} = {operations[operation](first_number, second_number)}")
#
#     confirmation = input(f"Type \'y\' to continue calculating with {operations[operation](first_number, second_number)}, or type \'n\' to start a new calculation: ").lower()
#
#     accumulator = operations[operation](first_number, second_number)
#
#     while confirmation == "y":
#         first_number = accumulator
#         for key in operations:
#             print(key)
#
#         operation = input("Pick an operation: ")
#
#         second_number = float(input("What's the next number?: "))
#
#         print(f"{first_number} {operation} {second_number} = {operations[operation](first_number, second_number)}")
#
#         accumulator = operations[operation](first_number, second_number)
#
#         confirmation = input(f"Type \'y\' to continue calculating with {operations[operation](first_number, second_number)}, or type \'n\' to start a new calculation: ")
#
#     print("\n" * 100)

# from art import art
# import random as rnd
#
# cards = [11, 2, 3, 4, 5 ,6 ,7, 8, 9, 10, 10, 10, 10]
#
# confirmation = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()
#
# while confirmation == "y":
#
#     print("\n" * 100)
#     print(art)
#
#     my_list = []
#     my_score = 0
#     my_first_card = cards[rnd.randint(0, len(cards) - 1)]
#     my_second_card = cards[rnd.randint(0, len(cards) - 1)]
#     my_list.append(my_first_card)
#     my_list.append(my_second_card)
#     for card in my_list:
#         my_score += card
#
#     computer_list = []
#     computer_score = 0
#     computer_first_card = cards[rnd.randint(0, len(cards) - 1)]
#     computer_second_card = cards[rnd.randint(0, len(cards) - 1)]
#     computer_list.append(computer_first_card)
#     computer_list.append(computer_second_card)
#     for card in computer_list:
#         computer_score += card
#
#     print(f"\tYour cards: {my_list}, current score: {my_score}")
#     print(f"\tComputer's first card: {computer_first_card}")
#
#     confirmation = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#
#     while confirmation == "y" and my_score <= 21:
#         my_new_card = cards[rnd.randint(0, len(cards) - 1)]
#         my_score += my_new_card
#         my_list.append(my_new_card)
#         if my_score > 21:
#             print(f"Your cards: {my_list}, current score: {my_score}")
#             print(f"Computer's first card: {computer_first_card}")
#             break
#         else:
#             computer_new_card = cards[rnd.randint(0, len(cards) - 1)]
#             computer_score += computer_new_card
#             computer_list.append(computer_new_card)
#
#         print(f"\tYour cards: {my_list}, current score: {my_score}")
#         print(f"\tComputer's first card: {computer_first_card}")
#         confirmation = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#
#     print(f"Your final hand: {my_list}, final score: {my_score}")
#     print(f"Computer's final hand: {computer_list}, final score: {computer_score}")
#     if my_score > 21:
#         if computer_score > 21:
#             if my_score > computer_score:
#                 print(f"You went over. You lose")
#             elif my_score < computer_score:
#                 print(f"Opponent went over. You win")
#             else:
#                 print(f"Draw!")
#         else:
#             print(f"You went over. You lose")
#     else:
#         if computer_score > 21:
#             print(f"Opponent went over. You win")
#         else:
#             if my_score < computer_score:
#                 print(f"You lose")
#             elif my_score > computer_score:
#                 print(f"You win")
#             else:
#                 print(f"Draw!")
#     confirmation = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


