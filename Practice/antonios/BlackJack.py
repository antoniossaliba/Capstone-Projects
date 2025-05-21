from art import art1
import random as rnd

cards = [11, 2, 3, 4, 5 ,6 ,7, 8, 9, 10, 10, 10, 10]

confirmation = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()

while confirmation == "y":

    print("\n" * 100)
    print(art1)

    my_list = []
    my_score = 0
    my_first_card = cards[rnd.randint(0, len(cards) - 1)]
    my_second_card = cards[rnd.randint(0, len(cards) - 1)]
    my_list.append(my_first_card)
    my_list.append(my_second_card)
    for card in my_list:
        my_score += card

    computer_list = []
    computer_score = 0
    computer_first_card = cards[rnd.randint(0, len(cards) - 1)]
    computer_second_card = cards[rnd.randint(0, len(cards) - 1)]
    computer_list.append(computer_first_card)
    computer_list.append(computer_second_card)
    for card in computer_list:
        computer_score += card

    print(f"\tYour cards: {my_list}, current score: {my_score}")
    print(f"\tComputer's first card: {computer_first_card}")

    confirmation = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    while confirmation == "y" and my_score <= 21:
        my_new_card = cards[rnd.randint(0, len(cards) - 1)]
        my_score += my_new_card
        my_list.append(my_new_card)
        if my_score > 21:
            print(f"Your cards: {my_list}, current score: {my_score}")
            print(f"Computer's first card: {computer_first_card}")
            break
        else:
            computer_new_card = cards[rnd.randint(0, len(cards) - 1)]
            computer_score += computer_new_card
            computer_list.append(computer_new_card)

        print(f"\tYour cards: {my_list}, current score: {my_score}")
        print(f"\tComputer's first card: {computer_first_card}")
        confirmation = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    print(f"Your final hand: {my_list}, final score: {my_score}")
    print(f"Computer's final hand: {computer_list}, final score: {computer_score}")
    if my_score > 21:
        if computer_score > 21:
            if my_score > computer_score:
                print(f"You went over. You lose")
            elif my_score < computer_score:
                print(f"Opponent went over. You win")
            else:
                print(f"Draw!")
        else:
            print(f"You went over. You lose")
    else:
        if computer_score > 21:
            print(f"Opponent went over. You win")
        else:
            if my_score < computer_score:
                print(f"You lose")
            elif my_score > computer_score:
                print(f"You win")
            else:
                print(f"Draw!")
    confirmation = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()