import random
class Dice:
    def roll(self):
        for i in range (2):
            print(random.randint(1, 6))

while True:
    command = input('> ').lower()
    if command == 'start':
        playing = True
        start_game = input('Welcome to the dice game! Would you like to roll? (Y) or (N): ').lower()
        if 'Y':
            playing == True
            print('Rolling the dice!')
            Dice.roll(self=0)
            again = input('Roll again? (Y) or (N): ').lower()
            if again == 'y':
                playing = True
                Dice.roll(self=0)
            elif again == 'n':
                playing = False
                print('See you next time!')
                break
            else:
                print('Please enter Y or N.')
        elif 'N':
            print('See you next time!')
        else:
            print('Please enter a valid command')
    else:
        print("Please enter 'start' to start the game.")