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
    if difficulty.casefold() == 'Easy'.casefold():
        return guess_count
    elif difficulty.casefold() == 'Hard'.casefold():
        return guess_count - 5 
    # Prevent invalid user input
    try:  
        print('Please enter a valid input.')
    except ValueError:
        print('Please enter a valid input.')


set_difficulty()
print(f'You have {guess_count} attempts remaining to guess a number')

def make_guess():
    print(f'You have {guess_count} attempts remaining to guess a number')
    guess = ('Make a guess: \n')
    if guess > secret_number:
        print('Too high!')
    

    