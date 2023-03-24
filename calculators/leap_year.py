print("Welcome to the Leap Year Calculator!")

while True:
    try: 
        year = int(input("Which year would you like to check?: ")) 
        break 
    except ValueError: 
        print("Please enter a valid year using numerical digits only")

if year % 4 == 0: 
  if year % 100 == 0: 
    if year % 400 == 0: 
      print(f'The year {year} is a Leap Year.')
    else:
     print(f'The year {year} is NOT a Leap Year.')
  else:
    print(f'The year {year} is a Leap Year.')
else: 
    print(f'The year {year} is NOT a Leap Year.')