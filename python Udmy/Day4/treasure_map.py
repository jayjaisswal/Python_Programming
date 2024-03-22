# line1 = [" "," "," "]
# line2 = [" "," "," "]
# line3 = [" "," "," "]
# map = [line1, line2, line3]
# print("Hiding your treasure! x marks the spot.")
# position = input("Where do you want to put the treasure?")

# spliting_input = position.split()
# if spliting_input[0] == "A":
#     spliting_input[0] = 0
# elif spliting_input[0] == "B":
#     spliting_input[0] = 1
# else:
#     spliting_input[0] = 2
    
    
# if spliting_input[1] == "1":
#     spliting_input[1] = 0
# elif spliting_input[1] == "2":
#     spliting_input[1] = 1
# else:
#     spliting_input[1] = 2


# print(spliting_input[0])
# print(spliting_input[1])
    

# map[spliting_input[1]][spliting_input[0]] = "x"


# print(f"{line1}\n{line2}\n{line3}")

# point to be notes that every entry in list is string

# Method 2

line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map = [line1, line2, line3]
print("Hiding your treasure! x marks the spot.")
position = input("Where do you want to put the treasure? :")

alphabet = position[0].lower()
letter = ["a", "b", "c"]
letter_index = letter.index(alphabet)

number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
