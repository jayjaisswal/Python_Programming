# ASCII Arts for rock, paper, and scissors by Veronica Karlsson

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
import random
print("Welcome type 1 for Rock ,2 for Paper and 3 for Scissors")
print('1. Rock\n2. Paper\n3. Scissors')
choice = input("Enter your choice :")

# game_image = [rock, paper, scissors]
# print(game_image[choice])---> Another way to print the images also can be used for comp

if choice == "1":
    print(f"Rock :{rock}")
elif choice == "2":
    print(f"Paper :{paper}")
elif choice == "3":
    print(f"Scissors :{scissors}")
else:
    print("invalid choice")

comp_choice = random.randint(0,3)
if comp_choice == 0:
    print(f"Rock :{rock}")
elif comp_choice == 1:
    print(f"Paper :{paper}")
elif comp_choice == 2:
    print(f"Scissors :{scissors}")


if (choice == "1" and comp_choice == 0) or (choice == "3" and comp_choice == 2) or (choice == "2" and comp_choice == 1):
    print("Game Draw")
elif choice == "1" and comp_choice == 1:
    print('You loose as "paper covers rock"')
elif choice == "1" and comp_choice == 2:
    print('You Win as "Rock crushes Scissors"')
    
elif choice == "2" and comp_choice == 0:
    print('You Win as "paper covers rock"')
elif choice == "2" and comp_choice == 2:
    print('You loose as "scissors cuts paper"')
    
elif choice == "3" and comp_choice == 0:
    print('You loose as "Rock crushes Scissors""')
elif choice == "3" and comp_choice == 1:
    print('You Win as "scissors cuts paper"')

    
