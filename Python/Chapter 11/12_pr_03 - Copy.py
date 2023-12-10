class Empolyee:
    salary = 2000
    increment = 4.7
    
    @property
    def salaryafterIncrement(self):
        return self.salary*self.increment
    
    @salaryafterIncrement.setter
    def salaryafterIncrement(self, sai):
        self.increment = sai/self.salary
        
e = Empolyee()
print(e.salaryafterIncrement)
print(e.increment)
e.salaryafterIncrement = 4300
print(e.salaryafterIncrement)
print(e.increment)
