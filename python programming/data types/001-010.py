# 001
a = "hello"
print(len(a))

# 002
lst = [1, 5, 23, 12]
print("sum of element in list is:",sum(lst))

# 003
def multiplylist(lst2):
    result = 1
    for x in lst2:
        result = result * x
    return result

lst2 = [12, 5, 6, 10, 19]
print(multiplylist(lst2))

import math
lst2 = [12, 5, 6, 10, 19]
a = math.prod(lst2)
print(a)

# 004
lst3 = [12, 45, 23, 9]

lst3.sort()
print(lst3[-1])

print(max(lst3))

# 005
lst4 = [23, 54, 90, 12, 9]
print(min(lst4))
lst4.sort()

print(lst4[0])

# 006
def count(xyz):
    dict = {}
    for n in xyz:
        keys = dict.keys()
        if n in keys:
            dict[n] = dict[n] + 1
        else:
            dict[n] = 1
    return dict

print(count("google.com"))

# 007
sample = "Google.com"

all_numb = {}
for n in sample:
    if n in all_numb:
       all_numb[n] = all_numb[n] + 1
    else:
        all_numb[n] = 1

print(str(all_numb))

# 008 
def enter_word(words):
    i = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            i += 1
    return i

print(enter_word(["a", "aa", "aaa", "b", "bb", "bbb"]))

# 009
def last(n):
        return n[-1]
    
def sort(tuples):
    return sorted(tuples, key=last)

tup = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("sorted:")
print(sort(tup))

def sort_tuple(tup):
    tup.sort(key = lambda x: x[-1])
    return tup

a = sort_tuple([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
print(a)

# 010

name = "sh"

if len(name) > 2:
    final = (name[0:2]) + (name[-2:])
    print(final)
else:
    print("")