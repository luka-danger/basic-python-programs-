import random

stages = ['''
   O
  /|\ 
 / | \ 
  / \ 
 /   \     
''', '''
   O
  /|\ 
 / | \ 
''','''
   O
  /|
 / | 
''','''
   O
   |
   |
''', '''
   O
''', '''

''']

stage_strings = ['''
Slender Man has caught you. There is no escape.
''', '''
Slender Man is getting closer. 
''','''
Slender Man is getting closer. 
''','''
You are being stalked by Slender Man.
''','''
Uh oh! You have been noticed by Slender Man.
''', '''
There is an ominous feeling in the air. Be careful! 
''']

word_list = ["cat", "dog", "cow", "monkey", "bird", "bear"]
secret_word = list(random.choice(word_list)) 
print(secret_word) #use for testing, then delete

lives = 5 
#To add "_" for every letter in chosen_word
display = []
word_length = len(secret_word)
for letter in range(word_length):
    display += "_"
print(display)
print(stage_strings[5])

#Use while loop to run code until all letters have been guessed
while "_" in display: 
    guess = input("Guess a letter: \n").lower()
    if letter != guess: 
        lives -= 1 
        print(stages[lives]) 
        print(stage_strings[lives])
#Replace "_" with letter if guess matches letter in chosen_word 
    for position in range(word_length): 
        letter = secret_word[position]   
#Reveals the letter in the correct position 
        if letter == guess:
            display[position] = letter 
            print(display)
#When all letters have been guessed, print "You won!" and break the while loop
    if "_" not in display: 
        print("You won!")
        break 
    elif lives == 0: 
        print("You lose")
        break 
