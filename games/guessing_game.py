# Choose random num 1 - 100
# Make function to set difficulty
# Let user guess number
# Make function to check user guess against actual answer
# Track number of turns and reduce by 1 if wrong
# Repeat guessing game if guess is wrong 

import random 

secret_number = random.randint(1, 100)
guess_count = 10

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100")

def set_difficulty():
    difficulty = input('Choose a difficulty. Type easy or hard: \n')
    if difficulty.casefold() == 'Hard'.casefold():
        return guess_count - 5
    elif difficulty.casefold() == 'Easy'.casefold():
        return guess_count
    # Prevent invalid user input
    try:  
        print('Please enter a valid input.')
    except ValueError:
        print('Please enter a valid input.')

def check_guess():
    if guess == secret_number: 
        print(f'You win! The number I was thinking was {secret_number}')
    elif guess > secret_number:
        print('Too high!')
    elif guess < secret_number: 
        print('Too low')
    elif guess_count == 0:
        print(f'You lose! The number I was thinking of was {secret_number}')
    else: 
        print('Please enter a valid integer: ')
    return guess_count - 1

set_difficulty()
print(guess_count)
while guess_count != 0:
    print(f'You have {guess_count} attempts remaining to guess a number')
    guess = int(input('Make a guess: \n')) 
    check_guess()
    
    

    