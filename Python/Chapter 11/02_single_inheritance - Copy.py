# This is single inheritance class

class empolyee:                 # This is Base class/Parent class
    company = "Microsoft"
    
    def myDetails(self):
        print("This is an empolyee")
        
class programmer(empolyee):    # This is Drived class/Child class
    company = "Google"
    languange = "Python"
    def proLang(self):
        print(f"The language is used by empolyee is {self.languange}.")
        
    def myDetails(self):
            print("This is an Googler")
        
e = empolyee()
e.myDetails()
p = programmer()
p.myDetails()
print(p.company)