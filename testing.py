def player_pos():
    #letting player make the move
    i = 0
    while i<1:
        player_choose = input('Please enter the position you want to go (1-9): ')
        if the_board[int(player_choose)] == 'X' or the_board[int(player_choose)] == 'O':
            print('This position has already been taken \n Please choose another position')
        elif the_board[int(player_choose)] == ' ':
            i += 1
            return player_choose

player_pos()