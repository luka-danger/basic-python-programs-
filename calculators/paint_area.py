import math


def paint_calc():
    # Calculates number of paint cans (Area / 5)
    # Ceiling function rounds up to nearest integer
    paintCans = math.ceil((height * width) / 5)
    print(f'You need {paintCans} cans of paint.') 

height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
paint_calc()