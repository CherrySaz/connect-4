import random

# game board, rows, cols, and player_1 and player_2 names here
board = []
cols = 7
rows = 6
player1_name = ""
player2_name = ""

# functions for the creation of the game
"""
This is the creation of the game, connect 4 boards.
The board has rows and columns.
Returns the game board in a list of lists.
"""


def create_board(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]


# current status of the board
def print_board(board):
    for row in board:
        row_str = ' | '.join(row)
        print(row_str)
        print(' - ' * (len(row) * 2 - 1))


# To check whether or not a move is valid.
# The 'move' consists of a player placing a 'token' in the column slot.
# Returns True if valid. If not, False.
def is_valid_move(board, col):
    if 0 <= col < len(board[0]):
        return board[0][col] == ' '
    else:
        return False


# The player (x or y) making a move / placing their token
def make_move(board, col, player):
    for row in reversed(board):
        if row[col] == '':
            row[col] = player
            break


# Generates a random move for the computer that must be valid
def computer_move(board):
    valid_moves = [col for col in range(len(board[0]))
                   if is_valid_move(board, col)]
    return random.choice(valid_moves)


# Check the winner by checking rows, vertically, horizontally, and diagonally
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


# Gameplay function
def play_game():
    global player1_name, player2_name, board

    board = create_board(rows, cols)  # Initialize the game board

    # Initialize variables and gather input from the user
    player1_name = input('Enter the name of Player 1 (x): ')
    player2_name = input('Enter the name of Player 2 (y): ')


game_mode = input('Choose a game mode(1 for player vs player,'
                  ' 2 for computer): ')

if game_mode == '1':
    player2_name = input(f'Enter the name of {player1_name}\'s opponent: ')
elif game_mode == '2':
    pass  # To continue without breaking
else:
    print('Invalid choice. Please enter 1 or 2')

players = {'x': player1_name, 'y': player2_name}
current_player = 'x'

while True:
    print_board(board)

    if current_player == 'x':
        # Inside the player's move input loop
        # Use strip to take out any whitespace
        while True:
            try:
                col_input = input(f"{players[current_player]} choose a column "
                                  f"(0 - {cols - 1}):").strip()
                if col_input.isdigit():
                    col = int(col_input)
                else:
                    print('Invalid input. Please enter a valid number.')
                if 0 <= col < cols:
                    break  # Exit the loop if the input is valid
                else:
                    print('Invalid column. ', end='')
                    print('Please choose a column within the valid range.')
                    continue  # continue the loop if invalid input
            except ValueError:
                print('Invalid input. Please enter a valid number.')

# Inside the computer's move logic
    if current_player == 'x':
        print(f'{players[current_player]} (computer) is thinking...'
              'please wait..')

    col = computer_move(board)
    print("Computer's selected column:", col)

    make_move(board, col, current_player)

    print_board(board)  # Display the updated board

    # Computer's turn
    if current_player == 'x':
        print(f'{players[current_player]} (computer) is thinking...'
              'please wait..')

        col = computer_move(board)

        make_move(board, col, current_player)

        if check_the_winner(current_player, board):
            print_board(board)
            print(f'{players[current_player]} wins!')
            break  # To break from the loop when a player wins
        elif all(cell != ' ' for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break  # To break from the loop in case of a tie

        # Toggle the current player for the next turn
        current_player = 'y' if current_player == 'x' else 'x'


if __name__ == '__main__':
    while True:
        play_game()
        play_again = input('Do you want to play again? (yes / no): ')
        if play_again.lower() != 'yes':
            break  # Exit the game loop gracefully
