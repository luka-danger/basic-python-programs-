# Given random height and width, create function to 
# calculate number of paint cans needed 
# H x W = Square Meters
# 1 can of paint per 5 sq m 
# (H * W) / 5 = Number of cans of paint
# Round up paint cans 



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)