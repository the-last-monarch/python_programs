class empolyee:
    company = "Microsoft"
    def getsalary(self):
        print(f"This empolyee working in {self.company} and recive {self.salary} as the salary. ")

Shadow = empolyee()
Shadow.salary = 100000       
Shadow.getsalary() # empolyee.getsalary(Shadow)