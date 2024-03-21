print("Name : Jay Kumar\nURN : 2203844 ")
side1 = int(input("Enter the Biggest side of triangle :"))
side2 = int(input("Enter the 2nd side of triangle :"))
side3 = int(input("Enter the 3rd side of triangle :"))
if side1**2 == side2**2+side3**2:
    print("Yes,it is a Right Angled Tringle")
else:
    print("Not a right Angled triangle")