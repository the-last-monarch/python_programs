from functools import reduce

a = lambda a,b : a+b

l = [1, 2, 3, 4, 5]

value = reduce(a, l)
print(value)