import random

# game board and player_1 and player_2 names here
board = []
cols = 7
player1_name = ""
player2_name = ""

# functions
"""
This is the creation of the game, connect 4 board.
The board has rows and columns.
Returns the game board in a list of lists.
"""


def create_board(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]


# currentstatus
'''current status of board'''


def print_board(board):
    for row in board:
        row_str = ' | '.join(row)
        print(row_str)
        print(' - ' * (len(row) * 2 - 1))


# gameplay
"""
To check whether or not a move is valid.
The 'move' consists of a player placing a 'token' in the column slot.
Return True if valid. If not, False.
"""


def is_valid_move(board, col):
    return board[0][col] == ' '


# Playing game
'''The player (x or y) making a move / placing their token'''


def make_move(board, col, player):
    for row in reversed(board):
        if row[col] == '':
            row[col] = player
            break


''' Generates a random move for the computer that must be valid'''


def computer_move(board):
    valid_moves = [col for col in range(len(board[0]))
                   if is_valid_move(board, col)]
    return random.choice(valid_moves)


'''
Check winner by checking rows, vertically, horizontally and diagonally
'''


def check_the_winner(player, board):
    # Checking Vertically
    for col in range(len(board[0])):
        for i in range(len(board) - 3):
            if all(board[i + j][col] == player for j in range(4)):
                return True

    # Checking horizontally
    for row in board:
        for i in range(len(row) - 3):
            if all(cell == player for cell in row[i:i + 4]):
                return True

    # Checking diagonally (top-left to bottom-right)
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            if all(board[i + k][j + k] == player for k in range(4)):
                return True

    # Checking diagonally (top-right to bottom-left)
    for i in range(len(board) - 3):
        for j in range(3, len(board[0])):
            if all(board[i + k][j - k] == player for k in range(4)):
                return True

    return False


def main():
    global player1_name, player2_name, board, cols

    # Initialize variables and gather input from the user
    rows = 6
    cols = 7
    board = create_board(rows, cols)

    player1_name = input('Enter the name of Player 1 (x): ')
    player2_name = input('Enter the name of player 2 (y): ')


while True:
    game_mode = input('Choose a game mode(1 for player vs player,'
                      ' 2 for player vs computer): ')
    if game_mode == '1':
        player2_name = input(f'Enter the name of {player1_name}\'s '
                             'opponent: ')
        break
    elif game_mode == '2':
        break
    else:
        print('Invalid choice. Please enter 1 or 2')


players = {'x': player1_name, 'y': player2_name}
current_player = 'x'

if __name__ == '__main__':
    main()

while True:
    print_board(board)

while True:
    if current_player == 'x':
        while True:
            try:
                col = int(input(f"{players[current_player]}, choose a column "
                                f"(0 - {cols - 1}):"))

                if col < 0 or col >= cols:
                    print('Invalid column. '
                          'Please choose a column within the valid range.')
                    continue
                else:
                    break  # Exit the loop if the input is valid
            except ValueError:
                print('Invalid input. Please enter a valid number.')

        if not is_valid_move(board, col):
            print('Column is full. Try again')
            continue
        thinking_message = (
            f'{players[current_player]} (computer) is thinking...'
            ' please wait..'
        )
        print(thinking_message)
        col = computer_move(board)

    make_move(board, col, current_player)

    if check_the_winner(current_player, board):
        print_board(board)
        print(f'{players[current_player]} wins!')
        break  # To break from loop when a player wins
    elif all(cell != ' ' for row in board for cell in row):
        print_board(board)
        print("It's a tie!")
        break  # To break from loop in case of tie

    # Toggle the current player for the next turn
    current_player = 'y' if current_player == 'x' else 'x'
