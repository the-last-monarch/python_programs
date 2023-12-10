a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
try:
    print(a/b)
except ZeroDivisionError as e:
    print("This is infinity")
