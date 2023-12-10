class calculator:
    def __init__(self, number):
        self.number = number
    
    def square(self):
        print(f"The square of the{self.number} is {self.number**2}")
    
    def squareroot(self):
        print(f"The squareroot of the{self.number} is {self.number**0.5}")
    
    def cube(self):
        print(f"The cube of the{self.number} is {self.number**3}")
    
a = calculator(int(input("Enter the value : ")))
a.square()
a.squareroot()
a.cube()