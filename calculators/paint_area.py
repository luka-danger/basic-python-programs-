# Given random height and width, create function to 
# calculate number of paint cans needed 
# H x W = Square Meters
# 1 can of paint per 5 sq m 
# (H * W) / 5 = Number of cans of paint
# Round up paint cans 

def paint_calc():
    area = (height * width) / 5
    print(f'You need {area} cans of paint.')

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
paint_calc()