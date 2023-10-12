count = 0
for i in range(4):
    for j in range(5):
        count = count + i * j
    print(count)
print(f'The final count: {count}')