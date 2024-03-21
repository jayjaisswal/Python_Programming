print("Welcome to the rollercoster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is yoyr age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("please pay $12.")
else:
    print("Sorry, you have to grow taller before you go to ride")