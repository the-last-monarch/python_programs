class Number:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, num2):
        print("Doing addition in class")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Doing multiplication in class")
        return self.num * num2.num
    
n1 = Number(4)
n2 = Number(6)
add = n1 + n2
print(f"{add}\n")
mul = n1 * n2
print(mul)