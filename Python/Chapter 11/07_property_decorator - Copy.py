class empolyee:
    company = "apple"
    salary = 6300
    bonusSalary = 700
    
    @property
    def totalSalary(self):
        return self.salary + self.bonusSalary
    
    @totalSalary.setter
    def  totalSalary(self, value):
        self.bonusSalary = value - self.salary
        
e = empolyee()
print(e.totalSalary)
e.totalSalary = 6500
print(e.salary)
print(e.bonusSalary)