is_prime = True

num = int(input("Enter number: \n"))
for i in range(2, num):
    if num % i == 0: 
        is_prime = False
        print(f'{num} is not a prime number.')