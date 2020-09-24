def checking_player_input(player_input):
    #Check if user input is a number between 1 to 9
    try:
        player_input = int(player_input)
    except ValueError:
        print('Error: Please only enter numbers')
        return False
    if player_input not in range(1,10):
        print("Error: Please only enter numbers between 1-9")
    else:
        return True