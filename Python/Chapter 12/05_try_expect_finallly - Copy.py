try:
    a = int(input("Enter a number: "))
    i = 1/a
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")
    