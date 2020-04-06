import numpy as np
import pandas as pd



def create_board():
    board_array = np.array([[' ',' ', ' '],[' ',' ', ' '],[' ',' ', ' ']])
    return board_array

def print_board(board):
    print (' {} | {} | {}' .format(board[0,0], board[0,1], board[0,2]))
    print ('-----------')
    print (' {} | {} | {}' .format(board[1,0], board[1,1], board[1,2]))
    print ('-----------')
    print (' {} | {} | {}' .format(board[2,0], board[2,1], board[2,2]))

def game_won(player, board):
    for row in range(3):
            if board[row, 0] == player and board[row, 1] == player and board[row,2] == player:
                return True
    for column in range(3):
            if board[0, column] ==player and board[1, column] == player and board[2, column] == player:
                return True
    if board[0,0] == player and board[1,1] == player and board[2,2] == player:
        return True
    if board[2,0] == player and board[1,1] == player and board[0,2] == player:
        return True

game_board = create_board()

player  = 'X'
game_board[2,0] = 'X'
game_board[1,1] = 'X'
game_board[0,2] = 'X'
print_board(game_board)
if game_won(player, game_board):
    print('Player: ' + player + ' wins!')
