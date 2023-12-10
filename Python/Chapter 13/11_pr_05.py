from functools import reduce
l = [1, 45, 6, 3, 65, 34, 90, 32]

a = reduce(max, l)
print(a)