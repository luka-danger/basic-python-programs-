file_lines = []

with open('my_file.txt') as f: 
    for line in f:
        file_lines.append(line.strip())

print(file_lines)




