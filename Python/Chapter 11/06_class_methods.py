class Employee:
    company ="razer"
    salary = 200
    location = "mumbai"
    
    # def changeSalary(self, sal):
        # self.__class__.salary = sal 
        
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal 
               
e = Employee()
print(e.salary)
e.changeSalary(400)
print(e.salary)
print(Employee.salary)