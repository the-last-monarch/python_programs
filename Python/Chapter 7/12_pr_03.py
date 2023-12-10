num = int(input("Enter the number: "))
prime = True
for a in range(2, num):
    if(num%a == 0):
        prime = False 
        break
if prime:
    print("This number is a Prime")
else:
    print("This number not is prime")
