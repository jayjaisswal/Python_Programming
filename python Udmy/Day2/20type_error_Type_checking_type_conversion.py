# type checking
num_char = len(input("What is your name?"))
# print("Your name is " + num_char + "characters.")
# TypeError: can only concatenate str (not "int") to str so

# type conversion
new_num_char = str(num_char)
print("Your name is " + new_num_char + " characters.")



# print(type(len(input("What is your name?"))))  #<class 'int'>
# num_char is integer and string and integer cannot add so

print(70 + float("100.7"))
print(str(67)+str(90))