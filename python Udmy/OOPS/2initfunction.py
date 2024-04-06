#creating class
class Student:
    def __init__(self, fullname):
        print("automatically called!!")
        self.name = fullname

#creating object(instance)
s1 = Student("jay")
print(s1.name) #-->jay


s2 = Student("Prince")
print(s2.name) #-->Prince



