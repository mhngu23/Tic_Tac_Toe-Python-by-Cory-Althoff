def isWinner(board,le):
    #Checking the Win Lose Condition
    return ((board[1] == le and board[2] == le and board[3] == le) or
        (board[1] == le and board[5] == le and board[9] == le) or
        (board[1] == le and board[4] == le and board[7] == le) or
        (board[2] == le and board[5] == le and board[8] == le) or
        (board[3] == le and board[5] == le and board[7] == le) or
        (board[3] == le and board[6] == le and board[9]) == le or
        (board[4] == le and board[5] == le and board[6]) == le or
        (board[7] == le and board[8] == le and board[9] == le))

def isTie(board):
    #Checking Tie Condition
    if '-' not in board:
        print('This is a tie')
        return True
    else:
        return False