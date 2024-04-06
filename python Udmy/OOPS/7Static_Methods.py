class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    #if we do not want to use self
    @staticmethod
    def hello():
        print("hello")
    def get_Average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"hi {self.name} , Your avg score is {sum/3}")
        

s1 = Student("jay", [55, 43, 54])
s1.get_Average() 

s1.name = "Prince"
s1.get_Average() 
s1.hello()
