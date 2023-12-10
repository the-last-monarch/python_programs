a = [4, 32, 87, 284, 73, 989]

# b= []
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

b = [i for i in a if i%2==0]
print(b)

t = [1, 3, 1, 4, 2, 4, 2, 2]
s = {i for i in t}
print(s)