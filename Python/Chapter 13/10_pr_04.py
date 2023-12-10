l = [5, 34, 85, 9845, 305, 345, 234, 98, 1, 98, 87, 36]

a = filter(lambda a: a%5==0, l)
print(list(a))