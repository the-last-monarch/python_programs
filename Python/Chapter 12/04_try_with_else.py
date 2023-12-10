try:
    a = int(input("Enter a number: "))
    i = 1/a
except Exception as e:
    print(e)
else:
    print("Your code run successfully")