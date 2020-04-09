

def create_board():
    board_array = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return board_array

def find_available_positions(board):
    available_positions = []
    for index, value in enumerate(board):
        if value == ' ':
            available_positions.append(index)
    return available_positions

def print_board(board):
    print (' {} | {} | {}' .format(board[0], board[1], board[2]))
    print ('-----------')
    print (' {} | {} | {}' .format(board[3], board[4], board[5]))
    print ('-----------')
    print (' {} | {} | {}' .format(board[6], board[7], board[8]))

def analyze_board(board, player_turn):
    pass
#    virtual_board = game_board
#    available_positions(virtual_board)
#    if board_full:
#        pass
#    if player_turn == 'human':
#        if game_won(board, player_turn):
#            return human_win
#        else analyze_board()

def game_won(board, player):
    for row in range(0,7,3):
        if board[row] == player and board[row+1] == player and board[row+2] == player:
            return True
    for column in range(0,3,1):
        if board[column] == player and board[column+3] == player and board[column+6] == player:
            return True
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

tie = 0
computer_win = 10
human_win = -10
player_turn  = 'X'

game_board = create_board()

human = input('Select X or O (X goes first):')

while not game_won(game_board, player_turn):
    print_board(game_board)
    print(find_available_positions(game_board))
    
    if player_turn == human:
        selected_board_position = input('Select your square (1-9):')
        game_board[int(selected_board_position)-1] = human
#    analyze_board(game_board, player_turn)

#if game_won(game_board, player_turn):
print_board(game_board)
print('Player: ' + player_turn + ' wins!')
