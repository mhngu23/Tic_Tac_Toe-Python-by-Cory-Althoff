round = 1
board = ['-' for x in range(10)]


def printBoard(board):
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
    #letting player make the move
    global board
    i = 0
    if '-' not in board:
        return print('There is no space left so this is a tie')
    else:
        print('Player turn')
        while i<1:
            player_choose = input('Please enter the position you want to go (1-9): ')
            if board[int(player_choose)] == 'X' or board[int(player_choose)] == 'O':
                print('This position has already been choosen \nPlease choose another position')
            elif board[int(player_choose)] == '-':
                i += 1
                return player_choose

def comp_pos():
    #random a computer move
    global board
    import random
    i = 0
    if '-' not in board:
        return print('This is a tie')
    else:
        print('Computer turn')
        while i < 1:
            comp_choose = random.randint(1,9)
            if board[int(comp_choose)] == 'X' or board[int(comp_choose)] == 'O':
                i = 0
            elif board[int(comp_choose)] == '-':
                print('Computer want to go into',comp_choose)
                i += 1
                return comp_choose

def isWinner(board,le):
    return ((board[1] == le and board[2] == le and board[3] == le) or
        (board[1] == le and board[5] == le and board[9] == le) or
        (board[1] == le and board[4] == le and board[7] == le) or
        (board[2] == le and board[5] == le and board[8] == le) or
        (board[3] == le and board[5] == le and board[7] == le) or
        (board[3] == le and board[6] == le and board[9]) == le or
        (board[4] == le and board[5] == le and board[6]) == le or
        (board[7] == le and board[8] == le and board[9] == le))


def Tic_Tac_Toe():
    #replace the position of user input into the board
    global round
    global board
    print('Welcome to Tic Tac Toe')
    printBoard(board)
    for i in range(len(board)):
        print('This is round ', round)
        if not(isWinner(board, 'X')) or not(isWinner(board, 'O')):
            board[int(player_pos())] = 'X'
            printBoard(board)
            board[int(comp_pos())] = 'O'
            printBoard(board)
        round += 1
        if isWinner(board, 'O') == True:
            print('You lost :( ')
            break
        elif isWinner(board, 'X') == True:
            print('You win!!!!!')
            break

Tic_Tac_Toe()