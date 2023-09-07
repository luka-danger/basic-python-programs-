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
for symbol in operations: 
    print(symbol)
should_continue = True 
    
while should_continue == True: 
    operator = input("Choose an operator from the line above: ") 
    # Remove any leading or trailing spaces in operator 
    operator = operator.strip()
    second_num = int(input("Enter second integer: ")) 
    calc_function = operations[operator]
    answer = calc_function(first_num, second_num)
    print(f'{first_num} {operator} {second_num} = {answer}' )
    
    keep_calculating = input(f'''Type 'y' to continue calculating with {answer}, 
    or type 'n' to exit: ''')
    if keep_calculating == 'y': 
        operator = input("Choose an operator from the line above: ") 
        operator = operator.strip()
        next_number = int(input("What's the next number?: "))
        new_answer = calc_function(answer, next_number)
    elif keep_calculating == 'n': 
        should_continue = False 

          


    
