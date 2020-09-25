def going_first_or_second():
    while True:
        player_turn = input('Please enter X if you want to go 1st or O if you want to go 2nd: ')
        if player_turn not in ['X','O']:
            print('Please only enter X or O')
        else:
            return player_turn
