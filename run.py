import random
import time


def print_board(board):
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n" + "-" * 29)


def check_win(board, player):
    # Check horizontally
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertically
    for col in range(7):
        for row in range(3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonally (from top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonally (from top-right to bottom-left)
    for row in range(3):
        for col in range(3, 7):
            if all(board[row + i][col - i] == player for i in range(4)):
                return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def player_move(board, player):
    while True:
        try:
            col = int(input(f"{player}, enter a column (1-7): ")) - 1
            if 0 <= col <= 6 and board[0][col] == " ":
                for row in range(5, -1, -1):
                    if board[row][col] == " ":
                        board[row][col] = player[0]
                        break
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def computer_move(board):
    print("Please wait... Computer is thinking...")
    time.sleep(2)
    while True:
        col = random.randint(0, 6)
        if board[0][col] == " ":
            for row in range(5, -1, -1):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break
            break


def play_game():
    board = [[" " for _ in range(7)] for _ in range(6)]

    if choice == "2":
        player1 = input("Enter the name of Player 1: ")
        player2 = input("Enter the name of Player 2: ")
    else:
        player1 = input("Enter your name: ")
        player2 = "Computer"

    while True:
        print_board(board)

        # Player 1's move
        player_move(board, player1)
        if check_win(board, player1[0]):
            print_board(board)
            print(f"{player1} wins!")
            break  # End the game

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break  # End the game

        print_board(board)

        # Player 2's move (or Computer's move in case of player vs computer)
        if choice == "2":
            player_move(board, player2)
        else:
            computer_move(board)

        if check_win(board, "O"):
            print_board(board)
            print(f"{player2} wins!")
            break  # End the game

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break  # End the game

            play_again = input("Do you want to play another game? (yes/no): ")
            play_again = play_again.lower()
            if play_again != "yes":
                break


if __name__ == "__main__":
    print("Welcome to Connect 4!")  # Welcome message
    print("1. Player vs Computer")  # Option 1
    print("2. Player vs Player")  # Option 2

    while True:
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("Player vs Computer")
            play_game()
        elif choice == "2":
            print("Player vs Player")
            play_game()
        else:
            print("Invalid choice. Please enter 1 or 2.")
