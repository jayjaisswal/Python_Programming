#creating class
class Student:
    name = "Jay kumar"
    def __init__(self):
        print("default constructor automatically called as object created.")
        print(self)  #--><__main__.Student object at 0x000001B959AAE990>

#creating object(instance)
s1 = Student()
print(s1)  #--><__main__.Student object at 0x000001B959AAE990>
print(s1.name)

#Constructor
# __init__() id default constructor automatically called as object created.