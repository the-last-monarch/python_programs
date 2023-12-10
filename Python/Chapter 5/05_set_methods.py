# creating an empty set
a = set()

# adding value in empty set 
a.add(1)
a.add(1)
a.add(3)
a.add(3) # adding a value repeatly dosen't change value fo a set
a.add(3)

# a.add([5, 7, 8])       # we cannot add list in sets
a.add((5, 7, 0))    # But we can add tuples in sets
# a.add({2:4})           # we cannot add dictionary also in sets
print(a)

print(len(a)) # print's the length of the set

# Removal of an item
a.remove(1) # will remove 1 from the set
# a.remove(12) # throws an error while removing 12 (which is not in set)
print(a)

# Remove any random value and then print it
print(a.pop())
print(a)

# clear the set 
print(a.clear)
print(a)

# print(a.union)