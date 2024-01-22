import random 

secret_number = random.randint(1, 100)
EASY_GUESS_COUNT = 10
HARD_GUESS_COUNT = 5

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100")

def set_difficulty():
    difficulty = input('Choose a difficulty. Type easy or hard: \n')
    if difficulty.casefold() == 'Hard'.casefold():
        return HARD_GUESS_COUNT
    elif difficulty.casefold() == 'Easy'.casefold():
        return EASY_GUESS_COUNT
    else:  
        print('Please enter a valid input.')
   

def check_guess(guess, secret_number, turns):
    if guess == secret_number: 
        print(f'You win! {secret_number} is the correct number.')
    elif guess > secret_number:
        print('Too high.')
        return turns - 1
    elif guess < secret_number: 
        print('Too low.')
        return turns -1 
    else: 
        print('Please enter a valid integer: ')

turns = set_difficulty()
guess = 0 
while guess != secret_number:
    print(f'You have {turns} attempts remaining to guess a number.')
    guess = int(input('Make a guess: ')) 
    check_guess(guess, secret_number, turns)
    turns -= 1
    if turns == 0 and guess != secret_number:
        print(f'You lose! The correct number was {secret_number}.')
        break

    