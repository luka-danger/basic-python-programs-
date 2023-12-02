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