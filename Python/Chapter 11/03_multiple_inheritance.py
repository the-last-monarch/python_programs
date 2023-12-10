class empolyee:
    company = "Microsoft"
    eCode = 96
    
class Freelancer:
    company = "Fiverr"
    level = 0
    
    def upgradeLevel(self):
        self.level = self.level + 1
    
class programmer(Freelancer, empolyee):   # if we change place of company then p.company will change also
    name = "Alive"

p = programmer()
p.upgradeLevel()
print(p.company)