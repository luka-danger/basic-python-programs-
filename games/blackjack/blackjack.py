import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []

computer_cards = []

def deal_card():
    deal_card = random.choice(cards)
    return deal_card
    

while True: 
    start_game = input('Do you want to play blackjack? (y) or (n):\n') 
    if start_game == 'y':
        deal_card()
    elif start_game == 'n':
        print('Boring!')
        break 
    else:
        print('Please enter valid option')