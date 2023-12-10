class Number:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, num2):
        print("Doing addition in class")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Doing multiplication in class")
        return self.num * num2.num
    
    def __str__(self):
        return (f"I am number {self.num}")
    def __len__(self):
        return 1
    
n = Number(1)
print(n)
print(len(n))
