print('''_________________________________________________________

         ///////
        || _  _|
        |/ .  .|
        (-   `\|      
         |  `-'|
    ____/   -  |___
   /  `\  .___/ |  \\
  |    `\      /'   |
  |   |  `\___/'  | |
_________________________________________________________                                               
                    ,----------------.
            /////// |Wh...Whats THAT?|    /`., ,
           || _  _| | Paisa !        |   /'/''<
           |/(O)(O) `-/--------------'_.'   /_'\.
           (-   `\|  /               (_ oOo __) |
            | _`-'| /                  `\:/'    `\\
       ____/ (___)|___                  /`       |____
      /  `\  .___/ |  \                /'\_______/ _  `\\
     /    `\      /'   \______ ____   |  |         |    |
    /   /   `\___/'  |        |  __)  |  |         |    |      
                
''')
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



#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

if direction == "left":
    destn = input('You\'ve come to lake. There is an island in the middle of lake. Type "wait" to wait for a boat. type "swim" to swim across.\n').lower()
    if destn == "wait":
        door = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of beasts. Game over.")
        elif door == "yellow":
            print("You found the tresure!. You Win!")
        else:
            print("You choose the wrong door! Game Over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game Over.")      
        
    