import random 

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

count = len(names) - 1
random_num = random.randint(1,int(count))
random_name = names[random_num]
print(f'{random_name} is going to buy the meal today!')