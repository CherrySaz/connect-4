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



 main()