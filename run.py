import random
import time

# Create game board with specified rows and columns


def create_board(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]

# Display current status of the game board


def print_board(board):
    for row in board:
        row_str = ' | '.join(row)
        print(row_str)
        print('- ' * (len(row) * 2 - 1))

# Check whether a move is valid in the given column


def is_valid_move(board, col):
    if 0 <= col < len(board[0]):
        return board[0][col] == ' '
    else:
        return False

# Make a move by placing a token in the specified column


def make_move(board, col, player):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = player
            break

# Generate a random move for the computer player


def computer_move(board):
    valid_moves = [col for col in range(len(board[0]))
                   if is_valid_move(board, col)]
    if valid_moves:
        return random.choice(valid_moves)
    else:
        return None  # No valid moves left

# Check if a player has won the game


def check_the_winner(player, board):
    for col in range(len(board[0])):
        for i in range(len(board) - 3):
            if all(board[i + j][col] == player for j in range(4)):
                return True

    for row in board:
        for i in range(len(row) - 3):
            if all(cell == player for cell in row[i:i + 4]):
                return True

    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            if all(board[i + k][j + k] == player for k in range(4)):
                return True

    for i in range(len(board) - 3):
        for j in range(3, len(board[0])):
            if all(board[i + k][j - k] == player for k in range(4)):
                return True

    return False

# Function to ask if players want to play again


def play_again():
    while True:
        choice = input('Do you want to play again? (yes / no): ').lower()
        if choice in ('yes', 'no'):
            return choice
        else:
            print('Invalid choice. Please enter "yes" or "no".')

# Main gameplay function


def play_game():
    while True:
        cols = 7
        rows = 6
        board = create_board(rows, cols)
        player1_name = input('Enter the name of Player 1 (x): ')
        game_mode = input('Choose a game mode (1 for player vs player, '
                          '2 for player vs computer): ')

        if game_mode == '1':
            player2_name = input('Enter the name of Player 2 (o): ')
        elif game_mode == '2':
            player2_name = "Computer"
        else:
            print('Invalid choice. Please enter 1 or 2')
            return

        players = {'x': player1_name, 'o': player2_name}
        current_player = 'x'

        while True:
            print_board(board)

            try:
                if current_player != 'Computer':
                    prompt = (
                       f"{players[current_player]} choose a column "
                       f"(0 - {cols - 1}): "
                    )
                    col_input = input(prompt).strip()
                    if col_input.isdigit():
                        col = int(col_input)
                        if 0 <= col < cols:
                            if is_valid_move(board, col):
                                make_move(board, col, current_player)
                                if check_the_winner(current_player, board):
                                    print_board(board)
                                    print(f'{players[current_player]} wins!')
                                    break
                                elif all(
                                    cell != ' '
                                    for row in board
                                    for cell in row
                                ):
                                    print_board(board)
                                    print("It's a tie!")
                                    break
                                # Switch players
                                if current_player == 'x':
                                    current_player = 'o'
                                else:
                                    current_player = 'x'
                            else:
                                print('Invalid column. Please choose a column '
                                      'within the valid range.')
                        else:
                            print('Invalid input. '
                                  'Please enter a valid number.')
                    else:
                        print('Invalid input. Please enter a valid number.')
                else:
                    print(f'{players[current_player]} '
                          'Please wait...Computer is thinking...')
                    time.sleep(2)  # Time delay while computer thinks
                    col = computer_move(board)
                    #  To get random move from index
                    if col is not None:
                        make_move(board, col, current_player)
                        if check_the_winner(current_player, board):
                            print_board(board)
                            print(f'{players[current_player]} wins!')
                            break
                        elif all(
                            cell != ' '
                            for row in board
                            for cell in row
                        ):
                            print_board(board)
                            print("It's a tie!")
                            break
                    # Switch player
                    current_player = 'x' if current_player == 'o' else 'o'

            except ValueError:
                print('Invalid input. Please enter a valid number.')

        choice = play_again()
        if choice == 'no':
            break


if __name__ == '__main__':
    play_game()
