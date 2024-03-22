print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))
payment =((total_bill * tip)/100 + total_bill)/people
new_payment = round(payment,2)
print(f"Each person should pay: ${new_payment}")