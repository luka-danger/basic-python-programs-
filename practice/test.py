def multiply(first_num, second_num):
    result = first_num * second_num
    return result 

def format_name(f_name, l_name):
    full_name = f_name.title() + " " + l_name.title()
    return full_name

print(multiply(12, 17))
print(format_name("nAtE", "edgE")) 

ask_name = input("First Name?: ")
ask_last_name = input ("Last Name?: ")
print(format_name(ask_name, ask_last_name))

# if i want to create multi line comments
# i can just write out my documentation as
# such and then when i am done i can highlight 
# the comment and command + / to create a docstring 