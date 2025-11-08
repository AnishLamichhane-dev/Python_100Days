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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("WElcome to the LaughTale Island.")
print("You are on a mission to find the ONE PIECE!!")
Left_Right = input(
    "You see a sign pointing left and another sign point right. Where do you want to go? Type 'Left' or 'Right' \n >>>")
Lower_Left_Right = Left_Right.lower()
if (Lower_Left_Right == "right"):
    print("You encouter Blackbeard and Die.")
elif (Lower_Left_Right == "left"):
    Swim_Wait = input(
        "You Encounter a river and see the Thousand Sunny Ship. Do you want to swim towards them or wait? Type 'Swim' or 'Wait' \n >>>")
    Lower_Swim_Wait = Swim_Wait.lower()
    if (Swim_Wait == "swim"):
        print("You are a devil fruit user.You can't swim in water. You died from drowning!")
    elif (Swim_Wait == "wait"):
        print("The Straw Hat Pirates see you stranded and come over to help you cross the river.")
        Door = input("You arived at the final destination for the One Piece.\nAmong the 3 doors ,one of them have the One Piece.\nDo you choose the Red, Blue or Yellow door? \nType 'Red or 'Blue' or 'Yellow' \n >>> ")
        Lower_Door = Door.lower()
        if (Lower_Door == "red" or Lower_Door == "blue"):
            print("You are caught by the marines chasing you and they capture you!")
        elif (Lower_Door == "yellow"):
            print("CONGRATULATIONS!!!")
            print("You found the One Piece and lived happily ever after...")
        else:
            print("Choose among the three doors(Red,Blue or Yellow)")
    else:
        print("Decide whether to Swim or Wait!")
else:
    print("Choose either Left or Right!")
