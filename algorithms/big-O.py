# Big O Notation 

# O(n)
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

# Drop Constants O(n)
# n + n = n 
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

# O(n^2)
# nxn = n^2
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j) 
