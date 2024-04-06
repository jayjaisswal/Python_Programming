class Car:
    def __init__(self):
        self.accelerator = False
        self.breakk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car started..")
        
car1 = Car()
car1.start()

#Hiding the implementation detail of a class and only showing the essential features to the users.

#Encapsulation
# Wrapping data and functions into a single unit (object).