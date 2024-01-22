# Global Scope 
# Variable, values, namespace exist and can be used anywhere
# Scope applies to anything you name (namespace): variables, functions, etc...
player_health = 10 

# Local Scope 
# Variable, values, namespace exist only inside the walls of a function 
# A nested function would is a local scope
# If you create variable within a function, it is only available within that funciton 
def drink_potion():
    potion_strength = 2
    print(f'Player Health: {player_health}')
    print(f'Potion Strength: {potion_strength}')

drink_potion()

# Be aware that where you are creating / naming something 
# will determine if it is a local or global scope 

# No such thing as block scope in Python 
# Blocks like if, while, and for don't count as local scope
# Variables created in these blocks can be used anywhere 
game_level = 3
enemies = ['Skeleton','Zombie', 'Alien']
if game_level < 5: 
    new_enemy = enemies[0]

print(f'New Enemy: {new_enemy}')

# Modifying Global Scope: 
enemies = 1

def increase_enemies():
    # (A1) Use global key word to modify a global variable inside funciton 
    # global enemies (remove #)
    # enemies += 1
    print(f'enemies inside function: {enemies}')
    # (B1) Return statement is a better way to use global scope in function
    return enemies +1 

increase_enemies()



'''If you create a global variable, and then use the same 
variable inside a local scope, this is actually a completely 
different varaible. 

Important -- You should not call your local and 
global variables the same thing! 

To modify a global variable inside of a function, 
refer to (A1) above. You probably don't want to modify
global scope inside functions very often. 

Another method to do this is to use the return statement (A2)
'''
