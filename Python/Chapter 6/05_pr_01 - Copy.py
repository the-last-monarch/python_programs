a = int(input("Enter your number first: "))
b = int(input("Enter your number second: "))
c = int(input("Enter your number third: "))
d = int(input("Enter your number forth: "))

if(a>d):
    f1 = a
else:
    f1 = d
if(b>c):
    f2 = b
else:
    f2 = c
if(f1>f2):
    print(str(f1) + " is the greatest number")
if(f2>f1):
    print(str(f2) + " is the greatest number")

# if(a>b):
#     print("This number 1 is greatest of all")
# elif(a>c):
#     print("This number 2 is greatest of all")
# elif(a>d):
#     print("This number 3 is greatest of all")
# elif(b>a):
#     print("This number 4 is greatest of all")
# elif(b>c):
#     print("This number 5 is greatest of all")
# elif(b>d):
#     print("This number 6 is greatest of all")
# elif(c>a):
#     print("This number 7 is greatest of all")
# elif(c>b):
#     print("This number 8 is greatest of all")
# elif(c>d):
#     print("This number 9 is greatest of all")
# elif(d>a):
#     print("This number 10 is greatest of all")
# elif(d>b):
#     print("This number 11 is greatest of all")
# elif(d>c):
#     print("This number 12 is greatest of all")

# else:
#     print("try again")