# Given random height and width, create function to 
# calculate number of paint cans needed 
# H x W = Square Meters
# 1 can of paint per 5 sq m 
# (H * W) / 5 = Number of cans of paint
# Round up paint cans 
import math

def paint_calc():
    paintCans = math.ceil((height * width) / 5)
    print(f'You need {paintCans} cans of paint.') 

height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
paint_calc()