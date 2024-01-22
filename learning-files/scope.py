enemies = 1

def increase_enemies():
    enemies = 2
    print(f'enemies inside function: {enemies}')

increase_enemies()
print(f'enemies outside function: {enemies}')

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