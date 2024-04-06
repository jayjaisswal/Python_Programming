#creating class
class Student:
    college_name = "GNDEC" #->class attributes
    #parameterized constructor
    def __init__(self, name, marks):
        self.name = name #--> Object attributes
        self.marks = marks
        print("automatically called!!")
        
    #method
    def Welcome(self):
        print("hello", self.name)
        
    def get_marks(self):
        return self.marks
        
        

#creating object(instance)
s1 = Student("jay", 76)
print(s1.name, s1.marks) 

print(Student.college_name)
print(s1.college_name)

s1.Welcome()
print(s1.get_marks() )
