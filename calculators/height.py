#When a user inputs heights (in cm)
#Count the number of inputted heights 
#Add heights together
#Divide the sum of heights by the total number of inputs
#Print the average height 

student_heights = input("Input a list of student heights\n").split()
#These lines place the inputted heights into a list
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n]) 

heights_in_list = 0 
total = 0
#Use for loop to find the number of heights in the list (Line 3)
for i in student_heights:
    heights_in_list+=1 

sum_of_heights = sum(student_heights)
average_height = sum_of_heights / heights_in_list
print(round(average_height)) 
