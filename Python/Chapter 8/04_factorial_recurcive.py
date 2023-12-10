# n! = 1 * 2 * 3 * 4 * ........ * n

#  using loop method to find factorial of a number
a = int(input("Enter the first number: "))
product = 1
for i in range(a):
    product = product * (i+1)
print(product)


# using loop and relation function to fin the factorial of a number
def factorial_ide(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

b = int(input("Enter the second number: "))
print(factorial_ide(b))


# using relation function to find factorial of a number
def factorial_recurcive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recurcive(n-1) 
c = int(input("Enter the third number: "))
print(factorial_recurcive(c))