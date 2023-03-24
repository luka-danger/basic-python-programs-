print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#Using new line character for cleaner output on terminal

lower1 = name1.lower() #to prevent code from breaking with capital letters
lower2 = name2.lower()
true_count1 = lower1.count("t") + lower1.count("r") + lower1.count("u") + lower1.count("e")
true_count2 = lower2.count("t") + lower2.count("r") + lower2.count("u") + lower2.count("e")
score1 = true_count1 + true_count2
love_count1 = lower1.count("l") + lower1.count("o") + lower1.count("v") + lower1.count("e")
love_count2 = lower2.count("l") + lower2.count("o") + lower2.count("v") + lower2.count("e")
score2 = love_count1 + love_count2
combine = str(score1) + str(score2) #Combine will combine the scores together ex: 1 + 2 = 12 
#rather than combine the scores using basic arithmetic ex: 1 + 2 = 3
score = int(combine) #This variable turns combine back into integers to run in the 
#if loop on the lower lines

if score < 10 or score > 90: 
    print(f'Your score is {score}, this will likely end in disaster!')
elif score >= 40 and score <= 50: 
    print(f'Your score is {score}, you are a perfect match!')
else:
    print(f'Your score is {score}, you should be alright together.')