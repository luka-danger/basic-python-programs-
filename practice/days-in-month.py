def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True 
      else:
        return False 
    else:
      return True 
  else:
    return False 
  

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    # Iterate through days in the month_days list
    for days in month_days:
        # Check if the month is 2 (February) during a leap year  
        # If it is a leap year and february, the function returns 29 days
        if is_leap(year) == True and month == 2: 
           days = 29
        else: 
            # Use month - 1 to prevent 'off by one' error 
            days = month_days[month - 1]
    return days 
  
  
#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days) 
