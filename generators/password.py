import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Empty list to assign characters into
char_list = []
#Creates range from 1 to number of characters user inputs 
#The +1 is to due to include all numbers in range
#Ex: Without +1, inputting 5 would give you up to 5, but not include 5
for char in range (1, nr_numbers + 1): 
#Append adds character to char_list
#Random.choice will choose numbers from our numbers list at random 
  char_list.append(random.choice(numbers))

for char in range(1, nr_letters + 1):
  char_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  char_list.append(random.choice(symbols))

#Shuffles the characters in the char_list, vs printing them in order, top down
random.shuffle(char_list)

#Pulls our shuffled characters out of list and puts into a string
password = ""
for char in char_list:
  password += char

print(f'Your password is: {password}')


