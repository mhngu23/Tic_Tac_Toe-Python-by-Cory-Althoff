from checking_player_input import checking_player_input
from checking_condition import isWinner, isTie

round = 1
board = ['-' for x in range(10)]
board[0] = '$'

def printBoard(board):
    #Print out the Board
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def player_pos():
    #Player movement
    global board
    i = 0
    print('Player turn')
    while i < 1:
        player_choose = (input('Please enter the position you want to go (1-9): '))
        if checking_player_input(player_choose) == True:
            if board[int(player_choose)] == 'X' or board[int(player_choose)] == 'O':
                print('This position has already been choosen \nPlease choose another position')
            elif board[int(player_choose)] == '-':
                i += 1
                return int(player_choose)

def comp_pos():
    #Computer movement
    global board
    import random
    i = 0
    print('Computer turn')
    while i < 1:
        comp_choose = random.randint(1,9)
        if board[int(comp_choose)] == 'X' or board[int(comp_choose)] == 'O':
            i = 0
        elif board[int(comp_choose)] == '-':
            print('Computer want to go into position',comp_choose)
            i += 1
            return int(comp_choose)


def Tic_Tac_Toe():
    #Main Function
    #global all parameters
    global round
    global board
    print('Welcome to Tic Tac Toe \nThis a 3*3 Tic Tac Toe board')
    printBoard(board)
    for i in range(len(board)):
        #provide the round number
        print('This is round ', round)
        #check if there is a winner yet
        if not(isWinner(board, 'X')) or not(isWinner(board, 'O')):
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
        #Update the round number
        round += 1

Tic_Tac_Toe()