class Animanls:
    animalType = "kutta"

class pets(Animanls):
    petName = "kalu"

class dogs(pets):
    @staticmethod
    def bark():
        print("bow, bow, bowwwwwww!")
        
a = Animanls()
p = pets()
d = dogs()
print(a.animalType)
print(p.petName)
d.bark()