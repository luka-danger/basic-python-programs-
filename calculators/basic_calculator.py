# Calculator Program
 
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator = {
    "+": add, 
    "-": subtract, 
    "*": multiply,
    "/": divide
}

first_num = int(input("Enter first integer: ")) 
second_num = int(input("Enter second integer: ")) 
for symbol in calculator: 
    print(symbol)
operator = input("Choose an operator from the line above: ")
calc_function = calculator[operator] 
answer = calc_function(first_num, second_num)

print(f'{first_num} {operator} {second_num} = {answer}' )
    
