# This solution doesn't need the math module
# Might need it for a better solution, so keeping so I don't forget
import math

num = int(input("Enter number: \n"))

# Any number less than 2 is not prime
if num < 2:
    print(f"{num} is not a prime number.")
# 2 is a prime number
elif num == 2:
    print(f"{num} is a prime number.")
# Any number divisble by 2, 3, or 5 is not prime
# 5 % 5 == 0, so added > 5 to avoid this
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 and num > 5:
    print(f"{num} is not a prime number.")
# Any number that doesn't fit above criteria will be a prime number
else:
    print(f"{num} is a prime number.")
