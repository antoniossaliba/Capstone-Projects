from data_of_coffee_machine import MENU
from data_of_coffee_machine import resources

total_money_inside_machine = 0.0

order = input("What would you like? (espresso/latte/cappuccino): ").lower()

while order != "espresso" and order != "latte" and order != "cappuccino" and order != "off" and order != "report":
    print("Your order is not valid! Please try again.")
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

while order != "off":
    if order == "report":
        for key in resources:
            if key  == "water":
                print(f"{key.capitalize()}: {resources[key]}ml")
            elif key == "milk":
                print(f"{key.capitalize()}: {resources[key]}ml")
            else:
                print(f"{key.capitalize()}: {resources[key]}g")
        print(f"Money: ${total_money_inside_machine}")
    else:
        enough_coins = False
        enough_resources = False
        if order == "espresso":
            type_of_coffee = MENU[order]
            ingredients = type_of_coffee["ingredients"]
            for ingredient in ingredients:
                if resources[ingredient] > ingredients[ingredient]:
                    enough_resources = True
                else:
                    print(f"Sorry there is not enough resources.")
                    enough_resources = False
                    break
        elif order == "latte":
            type_of_coffee = MENU[order]
            ingredients = type_of_coffee["ingredients"]
            for ingredient in ingredients:
                if resources[ingredient] > ingredients[ingredient]:
                    enough_resources = True
                else:
                    print(f"Sorry there is not enough resources.")
                    enough_resources = False
                    break
        else:
            type_of_coffee = MENU[order]
            ingredients = type_of_coffee["ingredients"]
            for ingredient in ingredients:
                if resources[ingredient] > ingredients[ingredient]:
                    enough_resources = True
                else:
                    print(f"Sorry there is not enough resources.")
                    refill = input("Do you want to refill the machine with resources? Type 'y' for yes or 'n' for no: ").lower()
                    while refill != "y" and refill != "n":
                        print("Remember you have to insert either 'y' for yes or 'n' for no.")
                        refill = input("Do you want to refill the machine with resources? Type 'y' for yes or 'n' for no: ").lower()
                    if refill == "y":
                        water = int(input("How many quantity of water do you want to add? (in ml): "))
                        resources["water"] += water
                        milk = int(input("How many quantity of milk do you want to add? (in ml): "))
                        resources["milk"] += milk
                        coffee = int(input("How many quantity of coffee do you want to add? (in g): "))
                        resources["coffee"] += coffee
                        print(f"Now the machine has the following resources after inserting new resources:")
                        print(f"Water: {resources['water']}ml")
                        print(f"Milk: {resources['milk']}ml")
                        print(f"Coffee: {resources['coffee']}g")
                    enough_resources = False
                    break

        if enough_resources:
            quarters = int(input("Enter number of quarters: "))
            dimes = int(input("Enter number of dimes: "))
            nickles = int(input("Enter number of nickles: "))
            pennies = int(input("Enter number of pennies: "))

            total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

            if MENU[order]["cost"] <= total:
                enough_coins = True
            else:
                print(f"Sorry that's not enough money. Money refunded.")

            if enough_coins and enough_resources:
                total_money_inside_machine += MENU[order]["cost"]
                type_of_coffee = MENU[order]
                ingredients = type_of_coffee["ingredients"]
                for ingredient in ingredients:
                    resources[ingredient] -= ingredients[ingredient]
                    if ingredient == "water":
                        print(f"{ingredient.capitalize()}: {resources[ingredient]}ml")
                    elif ingredient == "milk":
                        print(f"{ingredient.capitalize()}: {resources[ingredient]}ml")
                    else:
                        print(f"{ingredient.capitalize()}: {resources[ingredient]}g")
                print(f"Money: ${total_money_inside_machine}")
                if MENU[order]["cost"] < total:
                    print(f"Here is ${round(total - MENU[order]['cost'], 2)} dollars in change.")

                print(f"Here is your {order}. Enjoy!")
            else:
                print(f"Not enough money!")

    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    while order != "espresso" and order != "latte" and order != "cappuccino" and order != "off" and order != "report":
        print("Your order is not valid! Please try again.")
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

print("Machine turning off...\nMachine is turned off successfully!")
