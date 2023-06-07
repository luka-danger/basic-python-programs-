is_prime = True

num = int(input("Enter number: \n"))
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        print(f'{num} is not a prime number.')
        break
if num < 2:
    is_prime = False
    print(f'{num} is not a prime number.')
elif is_prime:
    print(f'{num} is a prime number.')