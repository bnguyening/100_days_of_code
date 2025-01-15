print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
road_decision = input("You come to a cross roads do you take the left or right trail?")
if road_decision == "right" or road_decision == "Right":
    lake_decision = input("The trail comes to a lake. Do you swim across or wait?")
    if lake_decision == "Wait" or lake_decision == "wait":
            print("You wait and the ferry appears. You get dropped off onto a building with three doors")
            door_decision = input("You see a red, yellow, and blue door. Which do you choose to go through?")
            if door_decision == "red" or door_decision == "Red":
                print("You enter a room of fire and get burnt to a crisp. Please try again")
            elif door_decision == "yellow" or door_decision == "Yellow":
                print("You made it to the treasure. You won!")
            elif door_decision == "blue" or door_decision == "Blue":
                print("You get eaten by tigers. Please try again")
            else:
                print("You failed to choose a door. Someone beat you to the treasure. Please try again")
    else:
            print("You get attacked by rainbow trout and die. Please try again")
else:
    print("You fall into a pit and die. Please try again")
