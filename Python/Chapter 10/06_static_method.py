class empolyee:
    company = "Microsoft"
    def getsalary(self, signature):
        print(f"This empolyee working in {self.company} and recive {self.salary} as the salary.\n{signature}")
    @staticmethod
    def greet():
        print("Thank you for working with us, sir")
Shadow = empolyee()
Shadow.salary = 100000  
Shadow.greet()
Shadow.getsalary("Thank you") # empolyee.getsalary(Shadow)
