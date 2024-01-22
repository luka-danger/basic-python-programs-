import random 

#Assign random number between 1 and 100
secret_number = random.randint(1, 100 + 1)
#Set guess count to 0
guess_count = 0
#Limit number of guesses to 7
guess_limit = 7
print('Guess a number between 1 and 100')
while guess_count < guess_limit:
    guess = int(input("Your Guess: "))
    #Add one count to guess each time 
    guess_count += 1
    if guess > secret_number:
        print("Guess lower")
    elif guess < secret_number:
        print("Guess higher")
    elif guess == secret_number:
        print('You won')
        break 
    elif guess_count == guess_limit:
        print('You lose')
        print(secret_number) 