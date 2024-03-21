print("Thankyou for choosing python pizza Delivery!")
size = input("What size of pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extre_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else :
    bill += 25
    
if add_pepperoni == "y":
    if size == "S" :
        bill+=2
    else:
        bill+=3

    

if extre_cheese == "Y":
    bill+=1
    
print("Thankyou for chhosing python Pizza Delivery")    
print(f"Your final bill is :${bill}")