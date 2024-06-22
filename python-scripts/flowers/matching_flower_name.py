flowers_dict = {}

def flower_dictionary():
    with open('flowers.txt') as flowers:
        flower_file = flowers.readlines()
    for flower in flower_file:
        key, value = flower.strip().split(':')
        flowers_dict[key.strip()] = value.strip()
    return flowers_dict


def find_flower_name():
    first_name = input("Enter your first name: ")
    letter = first_name[0]
    matching_flower = flowers_dict[f'{letter}']
    print(f'Your name is {first_name} and your matching flower is {matching_flower}')

flower_dictionary()
find_flower_name()