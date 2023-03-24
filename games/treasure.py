print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You will use (L) and (R) to make your decisions. ")
print("You begin your journey by walking uphill on a path. \
After walking half a mile, you reach a fork in the road. On the left \
is a dark forest, on the right is a gentle meadow.")
fork = input("Do you choose Left(L) or Right(R)?: \n")
if fork.casefold() == "l":
  print("You chose to enter the dark forest. After following a faint, winding path \
you approach another choice. On the right, there is a rope bridge \
crossing a steep cliff. Your other choice is to stay left and \
continue the path.")
  bridge = input("Do you choose Left(L) or Right(R)?: \n")
  if bridge.casefold() == "r":
    print("You chose to cross the rope bridge. It swings back and forth in \
the wind, but is surprising stable and you make it across safely. Shortly after the \
bridge, you approach a dark, ominous cave. It looks pretty dangerous.")
    cave = input("Do you choose Left(L) to turn around or Right(R) to go into the cave?: \n")
    if cave.casefold() == "r":
      print("You pull out your flashlight and walk into the dark cave. You notice that \
the cave cliffs out, but see a rope tied to a rock that will help you descend the \
cliff face.")
      rope = input("Do you take choose Left(L) to look around for a new route, or Right(R) to \
descend the rope? \n")
      if rope.casefold() == "l":
        print("You aren't going to take a chance with that old rope. You look around \
and surely enough, find another route. You find a tunnel that takes you deeper \
into the cave. The tunnel leads into a large room with two doors.")
        doors = input("Do you choose the door on the Left (L) or the door on the Right(R)?: \n")
        if doors.casefold() == "l":
          print("You chose the door on the left. You walk into the room and on the left side of \
the room you see a treasure box!")
          box = input("Do you open the box on the left side of the room (L) or turn around \
and head out the door on the right(R)?: \n")
          if box.casefold() == "l":
            print("You open up the treasure box...but it's empty. Some tasks just aren't worth doing.")
            print("*Sigh* You turn around and walk out the door and find a group of \
mutant cave dwellers waiting for you. You're dead!")
            print("THE END.")
          else: 
            print("You opt to not open the treasure box. You walk out the door and find a group of \
mutant cave dwellers waiting for you. You're dead!")
        else: 
          print("You chose the door on the right. You walk into the room. It was a trap! \
You fall into a hole filled with spikes. You're dead!")
      else:
        print("The rope seems safe enough. You being your descent.")
        print("SNAP! The rope breaks in half and you fall to your doom. You're dead!")
    else:
      print('Caves are Dangerous! You have seen the movie "The Descent". You turn around \
and cross the rope bridge. Halfway across, the rope snaps and you fall hundreds of \
feet. You are dead!')
  else: 
    print("You chose to take the path around. After following the path, you \
turn a corner and find yourself face to face with a hungry pack of wolves. \
You turn to run, but realize you're surrounded. You're dead!")
else: 
  print("You walk down the meadow. Everything is quiet until you hear a click. \
You realize the meadow was a mine field...but it's too late. You're dead!")
