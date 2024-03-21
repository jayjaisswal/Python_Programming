print("Welcome to the rollercoster!")
height = int(input("What is your height in cm?"))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7.")
    elif age>=45 and age <=55:
        print("Everything is going to be ok. HAve a free ride on us!")
    else:
        bill = 12
        print("Adult ticket are $12.")
    
    wants_photo = input("Do you want a photot taken? Y or N.")
    if wants_photo == "Y":
        if age>=45 and age <=55:
            bill = 0
        else:
            bill+=3 
        
    print(f"Your Final bill is {bill}")
    
else:
    print("Sorry, you have to grow taller before you go to ride")