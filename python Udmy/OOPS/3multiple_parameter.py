#creating class
class Student:
    #Default constructor
    def __init__(self):
        pass
    
    #parameterized constructor
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("automatically called!!")
        

#creating object(instance)
s1 = Student("jay", 76)
print(s1.name, s1.marks) 


s2 = Student("Prince", 88)
print(s2.name, s2.marks) 
