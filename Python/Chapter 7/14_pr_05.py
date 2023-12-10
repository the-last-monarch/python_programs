num = int(input("Enter the number: "))
factorial = 1
for a in range(1, num + 1):
    factorial = factorial * a
print(f"the factorial of {num} is {factorial}")