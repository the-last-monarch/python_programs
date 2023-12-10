def natural(n):
    if n <= 1:
        return n
    return  natural(n-1) + n

a = int(input("Enter the number: "))
print(natural(a))