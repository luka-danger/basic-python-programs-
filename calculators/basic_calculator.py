def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

first_num = int(input("Enter first integer: ")) 
second_num = int(input("Enter second integer: ")) 
for symbol in operations: 
    print(symbol)
operator = input("Choose an operator from the line above: ")
# Remove any leading or trailing spaces in operator 
operator = operator.strip()
calc_function = operations[operator]
answer = calc_function(first_num, second_num)

print(f'{first_num} {operator} {second_num} = {answer}' )
    
