#Function for printing the current state of the Tic Tac Toe board
def print_board(board):
    current_board = str()

    for i in range(len(board)):

        current_row = board[i]

        for j in range(len(current_row)):

            if j != len(current_row) - 1:
                current_board += '\t'
                current_board += current_row[j]
                current_board += '\t'
                current_board += '|'

            else:

                current_board += '\t'
                current_board += current_row[j]
                current_board += '\n'

        if i != len(board) - 1:

            current_board += '-------------------------\n'

    print(current_board)

#Function for checking if the game is over i.e. if one of the players won
def check_for_win(board):
    if board[0][0] == board[0][1] == board[0][2] != '':
        return True
    if board[1][0] == board[1][1] == board[1][2] != '':
        return True
    if board[2][0] == board[2][1] == board[2][2] != '':
        return True
    if board[0][0] == board[1][0] == board[2][0] != '':
        return True
    if board[0][1] == board[1][1] == board[2][1] != '':
        return True
    if board[0][2] == board[1][2] == board[2][2] != '':
        return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

#Function for checking if there is a draw i.e. when the board is fully filled
def check_for_draw(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '':
                return False
    return True

menu = input("Do you want to play? ('Yes' or 'No') ").lower()

while menu != 'yes' and menu != 'no':
    print("\nYou have to enter only 'Yes' or 'No'!")
    menu = input("Do you want to play? ('Yes' or 'No') ").lower()

while menu == 'yes':
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    print("\nNow, you have to choose for player 1 and player 2 either to be 'X' or 'O'\n")
    player_1 = input("Enter the symbol for player#1: ").lower()
    while player_1 != 'x' and player_1 != 'o':
        print("\nYou have to choose either 'X' or 'O'\n")
        player_1 = input("Enter the symbol for player#1: ").lower()
    if player_1 == 'x':
        player_1 = 'X'
        player_2 = 'O'
        print("\nPlayer#2 got automatically 'O'\n")
    else:
        player_1 = 'O'
        player_2 = 'X'
        print("\nPlayer#2 got automatically 'X'\n")
    choose_beginner_player = input("Which player do you want to start first? (Enter 1 or 2) ")
    while choose_beginner_player != '1' and choose_beginner_player != '2':
        print('\nYou have to choose either option 1 which indicates player#1 or 2 which indicates player#2\n')
        choose_beginner_player = input("Which player do you want to start first? (Enter 1 or 2) ")
    if choose_beginner_player == '1':
        starter = 0
    else:
        starter = 1
    print("\nLet the better win! Have fun!\n")
    while not check_for_win(board) and not check_for_draw(board):
        print("State of the board:\n")
        print_board(board)
        if starter % 2 == 0:
            print("\nPlayer 1 it is your turn\n")
        else:
            print("\nPlayer 2 it is your turn\n")
        print("\nWhere do you want to insert your symbol\n")
        row = input("Enter the row number: (From 1 to 3) ")
        while row != '1' and row != '2' and row != '3':
            print("\nYour options are 1, 2, or 3\n")
            row = input("Enter the row number: (From 1 to 3) ")
        column = input("Enter the column number: (From 1 to 3) ")
        while column != '1' and column != '2' and column != '3':
            print("\nYour options are 1, 2, or 3\n")
            column = input("Enter the column number: (From 1 to 3) ")
        while board[int(row) - 1][int(column) - 1] != '':
            print('\nThis cell is filled choose another one!\n')
            row = input("Enter the row number: (From 1 to 3) ")
            while row != '1' and row != '2' and row != '3':
                print("\nYour options are 1, 2, or 3\n")
                row = input("Enter the row number: (From 1 to 3) ")
            column = input("Enter the column number: (From 1 to 3) ")
            while column != '1' and column != '2' and column != '3':
                print("\nYour options are 1, 2, or 3\n")
                column = input("Enter the column number: (From 1 to 3) ")
        if starter % 2 == 0:
            board[int(row) - 1][int(column) - 1] = player_1
        else:
            board[int(row) - 1][int(column) - 1] = player_2
        starter += 1
    print("\nState of the board:\n")
    print_board(board)
    if check_for_draw(board):
        print('\nDraw!\n')
    else:
        if starter % 2 == 0:
            print("Player 2 won!")
        else:
            print("Player 1 won!")

    menu = input("\nDo you want to play? ('Yes' or 'No') ").lower()

    while menu != 'yes' and menu != 'no':
        print("\nYou have to enter only 'Yes' or 'No'!")
        menu = input("Do you want to play? ('Yes' or 'No') ").lower()

print("Closing Tic Tac Toe...")