class oneCell:
    species = "amoeba"
    def bloodType(self):
        print("This is one cell species")
        
class multiCell(oneCell):
    Type = "animals"
    
    def cellType(self):
        print(f"Animals are multi cell species{self.cell}")
        
    def bloodType(self):
        print("They are warm blooded")
        
class blood(multiCell):
    typeHeart = "warm"
        
    def cellType(self):
        print(f"these type have multiple cells")
            
    def bloodType(self):
        print("Humans are warm blooded")
        
o = oneCell()
o.bloodType()
print(o.species) 
print("\n")

m = multiCell()
m.bloodType()
print(m.Type)
print("\n")

b = blood()
b.bloodType()
print(b.typeHeart)
print(b.species)