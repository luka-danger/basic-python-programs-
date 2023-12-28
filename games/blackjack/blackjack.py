import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []

computer_cards = []

def deal_card():
    user_cards.append(random.choices(cards, k=2))
    computer_cards.append(random.choices(cards, k=2))
    print(f'Your cards: {user_cards}')
    print(f'Computer cards: {computer_cards}')
    
deal_card()