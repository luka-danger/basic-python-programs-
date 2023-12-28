import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []

computer_cards = []

def initial_deal():
    user_cards.append(random.choices(cards, k=2))
    computer_cards.append(random.choices(cards, k=2))
    print(f'Your cards: {user_cards}')
    print(f'Computer cards: {computer_cards}')

def hit():
    user_cards.append(random.choice(cards))
    print(f'Cards: {user_cards}')

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

