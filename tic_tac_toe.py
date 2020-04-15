
human = ' '
computer = ' '
player_turn  = 'X'

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

def analyze_board(virtual_board, player_turn):  
    if len(find_available_positions(virtual_board)) == 1:
        for index in find_available_positions(virtual_board):
            virtual_board[index] = player_turn
            if player_turn == human and game_won(virtual_board, player_turn):
                return -10
            elif player_turn == computer and game_won(virtual_board, player_turn):
                return 1000
            else:
                return 0
    move_score = {}
    if player_turn == 'human':
        for index in find_available_positions(virtual_board):
            move_score['index'] = index
            move_score['score'] = 1000000000
            virtual_board[index] = player_turn
            move_score['score'] =  min(move_score['score'], analyze_board(virtual_board, switch_player()))
            return move_score['index']
    else:
        for index in find_available_positions(virtual_board):
            move_score['index'] = index
            move_score['score'] = -100000000000
            virtual_board[index] = player_turn
            move_score['score'] =  max(move_score['score'], analyze_board(virtual_board, switch_player()))
            return move_score['index']

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

def switch_player():
    global player_turn
    if player_turn == 'X':
        player_turn = 'O'
    else:
        player_turn = 'X'
    return player_turn


game_board = create_board()

while human not in ['X', 'x', 'O', 'o']:
    human = str.upper(input('Select X or O (X goes first):'))
if human == 'X':
    computer = 'O'
else:
    computer = 'X'

while not game_won(game_board, player_turn):
    print_board(game_board)
    
    if player_turn == human:
        print("Player's turn:" + player_turn)
        selected_board_position = ' '
        while selected_board_position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            selected_board_position = input('Select your square (1-9):')
        if int(selected_board_position)-1 in find_available_positions(game_board):
            game_board[int(selected_board_position)-1] = player_turn
        if game_won(game_board, player_turn):
            break
#        switch_player()
    elif player_turn == computer:
        print("Player's turn:" + player_turn)
        virtual_board = list(game_board)
        computer_move = analyze_board(virtual_board, player_turn)
        print('Computer chooses: ' + str(computer_move+1))
        if computer_move in find_available_positions(game_board):
            game_board[computer_move] = player_turn
        if game_won(game_board, player_turn):
            break
    switch_player()

print_board(game_board)
print('Player: ' + player_turn + ' wins!')
