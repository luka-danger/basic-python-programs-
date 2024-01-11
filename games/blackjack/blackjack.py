import random

def deal_card():
    # Return random card from deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.choice(cards)
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21: 
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0: 
        return "You lose! The computer has a Blackjack 😱"
    elif user_score == 0:
        return "Blackjack! You win 😎"
    elif user_score > 21:
        return "You went over 21. You lose 😢"
    elif computer_score > 21:
        return "The computer went over 21. You win 😁"
    elif user_score > computer_score and user_score <= 21:
        return "You win 😁"
    else: 
        return "You lose 😢"

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over: 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f'Your cards: {user_cards}, Your score: {user_score}')
    print(f'Computer Card: {computer_cards[0]}')

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_selection = input("Hit or stay? Type 'h' to get another card, type 's' to pass; \n")
    if user_selection.casefold() == 'h':
        user_cards.append(deal_card())
    else:
        is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f'Your final hand: {user_cards}, final score: {user_score}')
print(f'Computer final hand: {computer_cards}, computer final score: {computer_score}')
print(compare(user_score, computer_score))