from checking_condition import isWinner, isTie
from checking_player_input import checking_player_input
from print_board import printBoard
from player_Information import player_information
from going_first_or_second import going_first_or_second

round = 1
board = ['-' for x in range(10)]
board[0] = '$'

def player_pos():
    #Player movement
    global board
    i = 0
    print('Player turn')
    while i < 1:
        player_choose = (input('Please enter the position you want to go (1-9): '))
        if checking_player_input(player_choose) == True:
            if board[int(player_choose)] == 'X' or board[int(player_choose)] == 'O':
                print('This position has already been taken \nPlease choose another position')
            elif board[int(player_choose)] == '-':
                i += 1
                return int(player_choose)

def comp_pos():
    #Computer movement
    import random
    global board
    print('Computer turn')

    possible_move = []

    for x in range(1, 10, 1):
        if board[int(x)] == '-':
            possible_move.append(x)

    for pos_winner_move in ['X','O']:
        for i in possible_move:
            board_Copy = board[:]   #you want to copy the whole board not just a reference to the original board
            board_Copy[i] = pos_winner_move
            if isWinner(board_Copy,pos_winner_move):
                comp_choose = i
                return comp_choose

    corners = []
    for i in possible_move:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners) > 0:
        comp_choose = random.choice(corners)
        return comp_choose

    if 5 in possible_move:
        comp_choose = 5
        return comp_choose

    edges = []
    for i in possible_move:
        if i in [2,4,6,8]:
            edges.append(i)
    if len(edges) > 0:
        comp_choose = random.choice(edges)
        return comp_choose

def Tic_Tac_Toe():
    #Main Function
    #global all parameters
    global round, board
    print('Welcome to Tic Tac Toe \nThis a 3*3 Tic Tac Toe board')
    printBoard(board)
    Player = player_information()
    Player.saving_information()
    player_turn = going_first_or_second()
    for i in range(len(board)):
        #provide the round number
        print('This is round ', round)
        #check if there is a winner yet
        if player_turn == 'O':
            if not(isWinner(board, 'X')) or not(isWinner(board, 'O')):
                board[(comp_pos())] = 'X'
                printBoard(board)
                if isWinner(board, 'X') == True:
                    print('You lost :( ')
                    break
                elif isWinner(board, 'O') == True:
                    print('You win!!!!!')
                    break
                elif isTie(board):
                    break
                board[(player_pos())] = 'O'
                printBoard(board)
                if isWinner(board, 'X') == True:
                    print('You lost :( ')
                    break
                elif isWinner(board, 'O') == True:
                    print('You win!!!!!')
                    break
                elif isTie(board):
                    break
        if player_turn == 'X':
            if not(isWinner(board, 'X')) or not(isWinner(board, 'O')):
                board[(player_pos())] = 'X'
                printBoard(board)
                if isWinner(board, 'O') == True:
                    print('You lost :( ')
                    break
                elif isWinner(board, 'X') == True:
                    print('You win!!!!!')
                    break
                elif isTie(board):
                    break
                board[(comp_pos())] = 'O'
                printBoard(board)
                if isWinner(board, 'O') == True:
                    print('You lost :( ')
                    break
                elif isWinner(board, 'X') == True:
                    print('You win!!!!!')
                    break
                elif isTie(board):
                    break
        #Update the round number
        round += 1

Tic_Tac_Toe()