import random
name_string = "Rana, Navin, Jay, Sushant"
names = name_string.split(", ")
# print(names)

num_items = len(names)
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today")

# import random

# name_string = ["Rana", "Navin", "Jay", "Sushant"]
# # No need to split name_string since it's already a list

# num_items = len(name_string)
# random_choice = random.randint(0, num_items - 1)

# person_who_will_pay = name_string[random_choice]

# print(person_who_will_pay + " is going to buy the meal today")


