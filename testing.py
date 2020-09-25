def checking_player_input(player_input):
    #check if user input is a number between 1 to 9
    try:
        player_input = int(player_input)
        asdf = 0
        while asdf == 0:
            if player_input > 9 or player_input < 1:
                print("Error: Please only enter numbers between 1-9")
            else:
                asdf = +1
                return int(player_input)
    except:
        print("Error: Please only enter numbers")

def player_pos():
    #player movement
    global board
    i = 0
    print('Player turn')
    while i < 1:
        player_choose = checking_player_input(input('Please enter the position you want to go (1-9): '))
        if board[int(player_choose)] == 'X' or board[int(player_choose)] == 'O':
            print('This position has already been choosen \nPlease choose another position')
        elif board[int(player_choose)] == '-':
            i += 1
            return player_choose
player_pos()