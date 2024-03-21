print("The Love Calculator is calculating your score...")
name1 = input("What is your Name :")
name2 = input("What is their Name :")
combined_names = name1 + name2
lower_name = combined_names.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_digit = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_digit = l + o + v + e

str_score = str(first_digit) + str(second_digit)
score = int(str_score)

if score >= 80:
    print(f"Your score is {score},you can go like coke and mentos.")
elif(score >= 40) and (score <= 79):
    print(f"Your score is {score},you can alright together.")
else:
    print(f"Your score is {score},Find Someone better!!!")
