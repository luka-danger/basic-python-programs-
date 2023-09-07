# Calculator Program
 
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def square_root(n1):
    return n1 * n1 

calculator = {
    "+": add, 
    "-": subtract, 
    "*": multiply,
    "/": divide, 
    "^": square_root
    }

first_num = input("Enter first integer: ")
second_num = input("Enter second integer: ")
math_function = input("Choose an operator: ")
for operator in calculator: 
    new_function = operator(first_num, second_num)
    print(new_function)
