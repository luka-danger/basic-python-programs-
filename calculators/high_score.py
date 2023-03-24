#When student scores are input as integers 
#Return the integers as a list and set it as a variable 
#Set variables for each number to 0 and create a new variable for highest score
#Compare each number in the list
#If the given number is the highest score
#That number is the new high score
#When all numbers have been compared, print the highest score 

student_scores = input("Input a list of student scores \n").split() 
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

num = 0 
highest_score = 0 
for num in student_scores:
    if num > highest_score:
        highest_score = num 
print(f'The highest score in the class is {highest_score}')