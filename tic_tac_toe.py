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

def analyze_board(board, player_turn):
    virtual_board = game_board
    available_positions
    if board_full:
        pass
    if player_turn == 'human':
        if game_won(board, player_turn):
            return human_win
        else analyze_board()

def game_won(board, player):
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

tie = 0
computer_win = 10
human_win = -10
player_turn  = 'X'

game_board = create_board()

human = input('Select X or O (X goes first):')

while not game_won:
    print_board(game_board)
    if player_turn == human:
        selected_board_position = input('Select your square (1-9):')
        game_board[selected_board_position]
    analyze_board(game_board, player_turn)

if game_won(player_turn, game_board):
    print('Player: ' + player + ' wins!')
