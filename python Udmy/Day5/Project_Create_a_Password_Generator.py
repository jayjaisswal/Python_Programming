# Generate a list containing all capital and small alphabets
# alphabet_list = [chr(i) for i in range(ord('A'), ord('Z')+1)] + [chr(i) for i in range(ord('a'), ord('z')+1)]

# print(alphabet_list)
import random
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbol = ['!', '@', '#', '$', '%', '&', '*', '_', '+']

print("Welcome to the password Generator!")

user_letter = int(input("How many letters would you like in your Password\n"))
user_symbol = int(input(f"How many sybmols would you like?\n"))
user_number = int(input(f"How many Numbers would you like?\n"))

#Easy level
# ghfh%$23 all are in order

# password = ""
# for char in range(1, user_letter + 1):
#     password += random.choice(letter)  #random.choice() is a fun
# for char in range(1, user_symbol + 1):
#     password += random.choice(symbol)
# for char in range(1, user_number + 1):
#     password += random.choice(number)
 
# print(password)
    

#hard level
# 2%gh$fg3 all are unordered


