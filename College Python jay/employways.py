print("Name : Jay Kumar\nURN : 2203844 ")
try:
    hourly_wage = float(input("Enter the hourly wage: Rs"))
    regular_hours = float(input("Enter the total regular hours: "))
    overtime_hours = float(input("Enter the total overtime hours: "))

    # Calculate regular pay
    regular_pay = hourly_wage * regular_hours

    # Calculate overtime pay
    overtime_pay = hourly_wage * 1.5 * overtime_hours

    # Calculate total weekly pay
    total_pay = regular_pay + overtime_pay

    print("Employee's total weekly pay is: Rs", total_pay)
except ValueError:
    print("Please enter valid numeric inputs.")
