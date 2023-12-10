class empolyee:
    company = "Microsoft"
    def __init__(self, name,salary, unit):
        self.name = name 
        self.salary = salary
        self.unit = unit
        print("Empolyee is working!")
    
    def getDetails(self):
        print(f"The name of the empolyee is {Shadow.name}")
        print(f"The salary of the empolyee is {Shadow.salary}")
        print(f"The company of the empolyee is {Shadow.company}")
        
    def getsalary(self, signature):
        print(f"This empolyee working in {self.company} and recive {self.salary} as the salary.\n{signature}")
        
        # In this method we don't need self attribute to run the program 
    @staticmethod
    def greet():
        print("Thank you for working with us, sir")
        
Shadow = empolyee("Shadow", 100, "Microsoft")
# Shadow = empolyee() --> This will throw an error

Shadow.getDetails()