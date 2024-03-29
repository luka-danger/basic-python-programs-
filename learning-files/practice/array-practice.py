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

# Will provide index of each value in num
for i, n in enumerate(num):
    print(i, n)

# Loop through arrays w/ unpacking
nums1= [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Reverse Array
nums1.reverse()
print(nums1)

# Sort Array
array1 = [6, 8, 19, 4, 2, 17]
array1.sort()
print(array1)
# Sort Array in Reverse 
array1.sort(reverse=True)
print(array1)