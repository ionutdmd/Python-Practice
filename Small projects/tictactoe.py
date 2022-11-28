import random


def display_board(board):
    for i in range(0, 9, 3):
        print('  |   | ')
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        print('  |   | ')
        if i < 6:
            print('---------')


def player_input(first):
    choice = 'wrong'

    while choice.upper() not in ['X', 'O']:
        choice = input(f"Player {first}: Do you want to be X or O? ")

        if choice.upper() not in ['X', 'O']:
            print("Invalid input")

    return choice.upper()


def place_marker(board, marker, position):
    board[position] = marker

    return board


def win_check(board, marker):
    if board[0] == board[1] == board[2] == marker or board[3] == board[4] == board[5] == marker or board[6] == board[
        7] == board[8] == marker or board[0] == board[4] == board[8] == marker or board[2] == board[4] == board[
        6] == marker or board[0] == board[3] == board[6] == marker or board[1] == board[4] == board[7] == marker or \
            board[2] == board[5] == board[8] == marker:
        return True
    return False


def choose_first():
    return random.randint(1,2)

def space_check(board,position):

    return board[position] == " "

def full_board_check(board):

    return board.count(' ') == 0

def player_choice(board):

    choice = 'wrong'

    while choice not in range(1,10):
        choice = int(input("Please select a position (1 - 9)"))

        if choice not in range(1,10):
            print("Invalid input")
        else:
            if choice in [1,2,3]:
                choice += 5
            elif choice in [4,5,6]:
                choice -= 1
            else:
                choice -= 7
            if space_check(board, choice):
                return choice
            else:
                choice = 'wrong'
                print('Position is occupied. Enter another position!')

def replay():
    choice = 'wrong'

    while choice.upper() not in ['Y', 'N']:
        choice = input("Do you want to play again? ")

        if choice.upper() not in ['Y', 'N']:
            print("Invalid input")
    if choice.upper() == 'Y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe')

while True:
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    first = choose_first()
    second = 3 - first
    first_marker = player_input(first)
    if first_marker == 'X':
        second_marker = 'O'
    else:
        second_marker = 'X'

    game_on = True

    while game_on:
        print('\n' * 100)
        display_board(board)
        print(f'Player {first} turn')
        first_choice = player_choice(board)
        place_marker(board,first_marker,first_choice)
        if win_check(board,first_marker):
            print(f'CONGRATULATIONS Player {first}!!!!!!!!!!!!!!!!!!!!! You won!')
            display_board(board)
            break

        if full_board_check(board):
            break
        print('\n' * 100)

        display_board(board)
        print(f'Player {second} turn')
        second_choice = player_choice(board)
        place_marker(board, second_marker, second_choice)
        if win_check(board,second_marker):
            print('\n' * 100)
            print(f'CONGRATULATIONS Player {second}!!!!!!!!!!!!!!!!!!!! You won!')
            display_board(board)
            break
    if not replay():
        break

