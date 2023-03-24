print("Welcome to the Treasure map! Enter your coordinates to mark where you'd like to \
hide the treasure. Ex: 00 would be the first box, 22 would be the last box")
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to hide your treasure?")

string = str(position)
coordinates = []
for i in string:
    coordinates.append(int(i))
x = coordinates[0]
y = coordinates[1]

if x == 0: 
    row = row1
elif x == 1:
    row = row2
else: 
    row = row3

row[y] = "X"
print(f"{row1}\n{row2}\n{row3}")