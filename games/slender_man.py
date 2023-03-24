import random

word_list = ["cat", "dog", "cow", "monkey", "bird", "bear"]
secret_word = list(random.choice(word_list)) 
print(secret_word) #use for testing, then delete

#To add "_" for every letter in chosen_word
display = []
word_length = len(secret_word)
for letter in range(word_length):
    display += "_"
print(display)

#Use while loop to run code until all letters have been guessed
#Replace "_" with letter if guess matches letter in chosen_word 
#The for loop reveals the letter in the correct position 
#When all letters have been guessed, print "You won!" and break the while loop
while "_" in display: 
    guess = input("Guess a letter: \n").lower()
    for position in range(word_length): 
        letter = secret_word[position]
        if letter == guess:
            display[position] = letter 
            print(display)
    if "_" not in display: 
        print("You won!")
        break 
