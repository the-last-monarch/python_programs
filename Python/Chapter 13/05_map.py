def square(num):
    return num*num
l = [2, 4, 6]
l2 = []

# Method 1
for item in l:
    l2.append(square(item))
print(l2)

# Method 2
print(list(map(square, l)))