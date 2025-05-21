
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {

    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


art = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|'''

while True:

    print(art)

    first_number = float(input("What's the first number?: "))

    for key in operations:
        print(key)

    operation = input("Pick an operation: ")

    second_number = float(input("What's the next number?: "))

    print(f"{first_number} {operation} {second_number} = {operations[operation](first_number, second_number)}")

    confirmation = input(f"Type \'y\' to continue calculating with {operations[operation](first_number, second_number)}, or type \'n\' to start a new calculation: ").lower()

    accumulator = operations[operation](first_number, second_number)

    while confirmation == "y":
        first_number = accumulator
        for key in operations:
            print(key)

        operation = input("Pick an operation: ")

        second_number = float(input("What's the next number?: "))

        print(f"{first_number} {operation} {second_number} = {operations[operation](first_number, second_number)}")

        accumulator = operations[operation](first_number, second_number)

        confirmation = input(f"Type \'y\' to continue calculating with {operations[operation](first_number, second_number)}, or type \'n\' to start a new calculation: ")

    print("\n" * 100)