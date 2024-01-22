import random 

secret_number = random.randint(1, 100)
guess_count = 10

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100")

def set_difficulty():
    difficulty = input('Choose a difficulty. Type easy or hard: \n')
    if difficulty.casefold() == 'Hard'.casefold():
        global guess_count
        guess_count -= 5
    elif difficulty.casefold() == 'Easy'.casefold():
        return guess_count
    else:  
        print('Please enter a valid input.')
   

def check_guess():
    if guess == secret_number: 
        print(f'You win! {secret_number} is the correct number.')
    elif guess > secret_number:
        print('Too high.')
    elif guess < secret_number: 
        print('Too low.')
    else: 
        print('Please enter a valid integer: ')

set_difficulty()

while guess_count != 0:
    print(f'You have {guess_count} attempts remaining to guess a number.')
    guess = int(input('Make a guess: ')) 
    check_guess()
    guess_count -= 1
    if guess == secret_number:
        break 

if guess_count == 0:
        print(f'You lose! The correct number was {secret_number}.')

    