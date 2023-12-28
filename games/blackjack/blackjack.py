cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
    print('Playing game!')

while True: 
    start_game = input('Do you want to play blackjack? (y) or (n):\n') 
    if start_game == 'y':
        play_game()
    elif start_game == 'n':
        print('Boring!')
        break 
    else:
        print('Please enter valid option')