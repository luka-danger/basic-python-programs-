#When a user inputs an integer (Line 8)
#Use a for loop to loop from the number one to the entered number (Line 10)
#If a number can be divided by 3 with no remainder, print "Fizz" (Line 13)
#If a number can be divided by 5 with no remainder, print "Buzz" (Line 15)
#If a number can be divided by both 3 and 5 with no remainder, print "FizzBuzz" (Line 11)
#Else print the entered number (Line 17)

enter_number = int(input("Please enter a number to FizzBuzz up to: \n")) 

for i in range(1, enter_number + 1): 
    if i%3 == 0 and i%5 == 0: 
        print("FizzBuzz")
    elif i%3 == 0: 
        print("Fizz")
    elif i%5 == 0: 
        print("Buzz")
    else:
        print(i)