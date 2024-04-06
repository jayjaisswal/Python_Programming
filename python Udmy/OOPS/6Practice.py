# class Student:
#     def __init__(self, name, phy, eng, maths):
#         self.name = name
#         self.phy = phy
#         self.eng = eng
#         self.maths = maths
        
#     def get_Average(self):
#         avg = (self.phy + self.eng + self.maths)/3
#         print(f"the avg marks of {self.name} is {avg}")
        

# s1 = Student("jay", 55, 43, 54)
# s1.get_Average() 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
        
    def get_Average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"hi {self.name} , Your avg score is {sum/3}")
        

s1 = Student("jay", [55, 43, 54])
s1.get_Average() 

s1.name = "Prince"
s1.get_Average() 

    