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
  

def days_in_month(month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    for days in month_days: 
        if is_leap(2000) == True: 
           days = 29
        else: 
            days = month_days[month - 1]
    print(days)


  
  
#🚨 Do NOT change any of the code below
days_in_month(2)
''' days = days_in_month(year, month)
print(days) ''' 
