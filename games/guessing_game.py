import random 

secret_number = random.randint(1, 100)
guess_count = 10

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100")

while guess_count != 0: 
    difficulty = input('Choose a difficulty. Type easy or hard: \n')
    if difficulty.casefold() == 'Hard'.casefold():
        guess_count -= 5
        print(guess_count)
        break
    elif difficulty.casefold() == 'Easy'.casefold():
        print(guess_count)
        break 
    else: 
        print('Please enter a valid input.')