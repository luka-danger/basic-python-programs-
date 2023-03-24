print("Welcome to the tip calculator! Don't forget to tip your server! ")

bill = float(input("What was the total bill?: ")) 
tip = float(input("What percentage tip would you like to give? 18, 20, or 22? "))
split = float(input("How many people to split the bill? "))
percent = (0.01 * float(tip)) + 1 
total = round((bill * percent) / split , 2) 
total_tip = (total - bill)
format_total_tip = float(total_tip)

print(f'Each person should tip ${format_total_tip}, for a total of ${total}')