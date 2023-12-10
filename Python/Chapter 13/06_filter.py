def lesser_than_5(num):
    if num<5:
        return True
    else:
        return False
        
g234wr = lambda num: num>10
l = [1,2,3,4,5,6, 86, 98]
a = (list(filter(lesser_than_5, l)))
b = (list(filter(g234wr, l)))
print(a)
print(b)