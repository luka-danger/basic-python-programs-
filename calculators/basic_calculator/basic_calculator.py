from logo import logo 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2 

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": exponent
}

def calculator(): 
    print(logo) 
    first_num = float(input("Enter first integer: ")) 
    for symbol in operations: 
        print(symbol) 
    should_continue = True 

    while should_continue:
        operator = input("Choose an operator from the line above: ") 
        # Remove any leading or trailing spaces in operator 
        operator = operator.strip()
        second_num = float(input("Enter next integer: ")) 
        calc_function = operations[operator]
        answer = calc_function(first_num, second_num)
        
        print(f'{first_num} {operator} {second_num} = {answer}' )
        
        keep_calculating = input(f"Type 'y' to continue calculating with {answer}, \
type 'n' to start a new calculator, or 'e' to exit: ")
        if keep_calculating == 'y': 
            first_num = answer 
        elif keep_calculating == 'n': 
            should_continue = False 
            calculator()
        elif keep_calculating == 'e': 
            break 
        else: 
            print("Please enter a valid selection.")
            break 

calculator()
    
