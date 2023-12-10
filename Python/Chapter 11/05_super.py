class oneCell:
    species = "amoeba"
    def __init__(self):
        print("all of us are made up of cells")
        
    def bloodType(self):
        print("This is one cell species")
        
class multiCell(oneCell):
    Type = "animals"
    
    def __init__(self):
        super().__init__()
        print("we are madeup of so many cells")
    
    def cellType(self):
        print(f"Animals are multi cell species{self.cell}")
        
    def bloodType(self):
        super().bloodType()
        print("They are warm blooded")
        
class blood(multiCell):
    typeHeart = "warm"
    
    def __init__(self):
        super().__init__()
        print("what is cell")
        
    def cellType(self):
        print(f"these type have multiple cells")
            
    def bloodType(self):
        super().bloodType()
        print("Humans are warm blooded")
        
# o = oneCell()
# o.bloodType()
# print(o.species) 

# m = multiCell()
# m.bloodType()
# print(m.Type)

b = blood()
# b.bloodType()
# print(b.typeHeart)
# print(b.species)