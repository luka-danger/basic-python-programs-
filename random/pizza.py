print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want to add Vegan Pepperoni? Y or N ")
extra_veggies = input("Do you want extra veggies? Y or N ")

small = 15
medium = 20
large = 25
bill = 0 

if size == "S": #S changes the bill to $15
    bill = small
elif size == "M": #M changes the bill to $20
    bill = medium
elif size == "L": #L changes the bill to $25
    bill = large 
else: 
    while size == "": 
        print('Invalid Selection. Please choose "S", "M", or "L".')
        if size == "S" or "M" or "L": 
            break 
    #This prevents the code from breaking if the user 
    #selects an input other than "S", "M", or "L"
if add_pepperoni == "Y": #Y adds $2 to the bill
    bill += 2
if extra_veggies == "Y": #Y adds $1 to the bill 
    bill += 1 

print(f'Your total is ${bill}.')