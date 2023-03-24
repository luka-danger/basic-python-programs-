#This code can be used to solve the 'Hurdle 4' problem on 
#Reeborg's World (reeborg.ca). The purpose of the game is to 
#Move Reeborg the Robot over a series of random hurdles that 
#Vary in height and distance apart by using Python code and a 
#Series of pre-built commands and condtions. 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(): 
    while front_is_clear():
        move()
        if right_is_clear():
            turn_right() 

while not at_goal():
    if wall_in_front(): 
        turn_left()
        jump() 
    else: 
        move()