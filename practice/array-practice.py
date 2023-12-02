# Arrays (Called Lists in Python)
arr = [1, 2, 3]
print(arr)

# Can be used as a stack 
arr.append(4)
arr.append(5)
print(arr)

# Combine lists
arrgghh = ['a', 'b', 'c']
arr.extend(arrgghh)
print(arr)

# Remove last value 
arr.pop()
print(arr)

arr[0] = 'hello'
print(arr)

n = 5
apple = [1] * n
print(apple)
print(len(apple))

# Sublists (slicing)
bbb = [1, 2, 3, 4, 5]
print(bbb[1:3])

# Unpacking 
a, b, c = [1, 2, 3]
print(c)

# Loop through arrays and add 
# Expected output [1, 7, 2, 7, 3, 7]
num = [1, 2, 3]
new_num = [] 

for i in num:
    new_num.append(i)
    new_num.append(7)

print(new_num)