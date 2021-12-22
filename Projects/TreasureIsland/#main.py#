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
 _________|___________| ;`-.o`"=._; ." ` '`."`` . "-._ /_______________|_______
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
print("Your mission is to find the treasure.\n")
start = input("Are you sure you want to continue (Y or N)? ")
start = start.lower()
if start == "y" or start == "yes":
    print("Alright then! Let's go!\n")
else:
    print("Don't worry! Take your time!\n")
    exit("GAME OVER\n")

# Go right or left
print("Seems like the starting point is an impasse. ")
direction = input("Would you like to go left(L) or right(R)? ")
direction = direction.lower()
if direction == "l" or direction == "left":
    print("Hooray! You were right! We can continue on our path!\n")
else:
    print("Pity! You fell into a hole and died!\n")
    exit("GAME OVER\n")

# Swim or wait
print("There is a tree on our path, but I can see a river from here.")
action = input("Would you like to swim(S) or wait(W)? ")
action = action.lower()
if action == "w" or action == "wait":
    print("Hooray! The wind freed the way.")
    print("The treasure is near, I can feel it! Let's continue!\n")
else:
    print("Pity! You were attacked by a trout and died!\n")
    exit("GAME OVER\n")

# Choose a door
print("Three different doors are in front of us! Only one leads to the treasure.")
door = input("Which door would you like to open: Red(R), Yellow(Y), or Blue(B)? ")
door = door.lower()
if door == "y" or door == "yellow":
    print("Unbelievable, that was the right door! My friend we found the treasure!\n")
    print("WE ARE RICH!\n")
elif door == "r" or door == "red":
    print("Pity! Not the right door! You were burned by the fire!\n")
    print("GAME OVER\n")
elif door == "b" or door == "blue":
    print("Pity! Not the right door! You were eaten by the beasts!\n")
    print("GAME OVER\n")
else:
    print("Why did you give up! We were almost there!\n")
    print("GAME OVER\n")

