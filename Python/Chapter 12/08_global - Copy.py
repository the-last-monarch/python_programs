a = 34   # global variable
def num1():
    global a  
    print(f"This is statement 1:{a}")
    a = 98    # local variable  # this will change value of a in whole code
    print(f"This is statement 2:{a}")
    
num1()
print(f"This is statement 3:{a}")