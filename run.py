import random

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
        print('|'.join(row))
    print('-' * (len(row) * 2 - 1))


# gameplay
"""
To check whether or not a move is valid.
The 'move' consists of a player placing a 'token' in the column slot.
Return True if valid. If not, False.
"""

def is_vaild_move():
    return board[0][col]==''


# Playing game
    '''The player (x or y) making a move / placing their token'''  
def make_move(board, col, player):
    for row in reversed(board):
        if row[col] =='':
            row[col] = player
            break


''' Generates a random move for the computer that must be valid'''
def computer_move(board):
    valid_move = [col for col in range(len(board[0}])) if is_a_valid_move(board, col)]
    return random.choice(valid_move)

'''Check winner by checking rows, vertically, horizontally and diagonally'''
    def check_the_winner(player, board):
        #Checking Vertically
        for col in range(len(board[0])):
            for i in range(len(board) - 3):
                if all(board[i + j][col] == player for j in range(4))
                return True

        #Checking horizontally
        for row in board:
            for i in range (len(row) - 3):
                if all (cell == player for cell in row[i:i+4])
                return True


         #Checking diagonally
         for i in range(len(board) - 3):
            for j in range(len(board[0]) - 3)
            if all (board [i + k][j + k] == player for k in range(4)):
                return True
                if all (board[i + 3 - k][j + k] == player in range(4)):
                    return True

    return False


    def main():
        #Initialize variables and gather input from user
         rows = 6
         cols = 7
         board = create_board(rows, cols)

         player1_name = input('Enter the name of Player 1 (x):')
         player2_name = input('Enter the name of player 2 (y):')       










 main()
