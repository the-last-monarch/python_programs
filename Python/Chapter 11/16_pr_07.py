class Vector:
    def __init__(self, vec):
        self.vec = vec
        
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]
    
    def __add__(self, vec2):
        newlist = []
        for i in range (len(self.vec)):
            newlist.append(self.vec[1] + (vec2.vec)[i])
        return Vector(newlist)
    def __mul__(self, vec2):
        value = 1
        for i in range (len(self.vec)):
            value += (self.vec[1] * (vec2.vec)[i])
        return value
    
    def __len__(self):
        return len(self.vec)
    
v1 = Vector([8, 6])
v2 = Vector([7, 3])
print(v1 + v2)
print(v1 * v2)
print(len(v1))
print(len(v2))