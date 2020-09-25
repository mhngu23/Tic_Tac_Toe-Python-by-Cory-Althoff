'''This function asks for player information and save them in a text file for later uses'''
class player_information():
    def __init__(self):
        self.name = input('Please enter your user name: ')
        while True:
            try:
                self.age = int(input('Please enter your age: '))
                break
            except ValueError:
                print('Error: Please only enter numbers')

    def saving_information(self):
        file = open('player_information.txt', 'a+')
        file.write('The name of the player is %s\r\n' % self.name)
        file.write('The age of the player is %d\r\n' % self.age)










