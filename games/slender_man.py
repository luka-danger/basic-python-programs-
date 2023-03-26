import random

logo = '''

'''
print(logo)

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
secret_word = random.choice(word_list)

lives = 5 
#To add "_" for every letter in chosen_word
display = []
word_length = len(secret_word)
for letter in range(word_length):
    display += "_"
print(stage_strings[5])
print(f"{' ' .join(display)} \n")

#Use while loop to run code until all letters have been guessed
while "_" in display: 
    guess = input("Guess a letter: \n").lower() 
    #Reduce lives by 1 each time an incorrect word is guessed
    if guess not in secret_word:  
        lives -= 1 
        print(stages[lives]) 
        print(stage_strings[lives])
    #Replace "_" with letter if guess matches letter in chosen_word 
    for position in range(word_length): 
        letter = secret_word[position]   
        #Reveals the letter in the correct position 
        if letter == guess:
            display[position] = letter 
    print(f" \n{' ' .join(display)} \n")
    #When all letters have been guessed, print "You won!" and break the while loop
    if "_" not in display: 
        print("You win! You are safe from Slender Man...for now.")
        break 
    elif lives == 0: 
        print("You lose.")
        break 
