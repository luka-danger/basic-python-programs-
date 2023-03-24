import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

 
choice = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n') 
print("Rock,\nPaper,\nScissors,\nShoot!")
if choice == "0": 
    print(f"You chose Rock. {rock}")
elif choice == "1": 
    print(f"You chose Paper. {paper}")
else: 
    print(f"You chose Scissors. {scissors}")

computer = random.randint(0,2)
if computer == 0:
    print(f"Computer chose Rock. {rock}")
    if choice == "0":
        print("It's a tie.")
    elif choice == "1": 
        print("You win!")
    else:
        print("You lose.")
elif computer == 1: 
    print(f"Computer chose Paper. {paper}")
    if choice == "0": 
        print("You lose.")
    elif choice == "1": 
        print("It's a tie.")
    else:
        print("You win!")
else: 
    print(f"Computer chose Scissors. {scissors}")
    if choice == "0":
        print("You win!")
    elif choice == "1": 
        print("You lose.")
    else:
        print("It's a tie.")