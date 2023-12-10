# 011
# str = "Shadow"
# modifiy_char = ""

# for char in range(0, len(str)):
    
#     if (str[char] == 's' or str[char] == 's'.upper()):
#         modifiy_char = modifiy_char + '$'
    
#     else:
#         modifiy_char = modifiy_char + str[char]

# print(modifiy_char)

# 012
# a = "abc"
# b = "xyz"

# new_a = a[:2] + b[2:]
# new_b = b[:2] + a[2:]
# print(new_a)
# print(new_b)

# print(new_a +' '+ new_b)

# 013

# a = "rose"

# if len(a)<=3:
#     print(a)
    
# elif a.endswith("ing"):
#     print(a + "ly")
    
# else:
#     print(a + "ing")

# 014

# x = "The lyrics is not that poor!"

# if x.endswith("not that poor!"):
#     print(x.replace("not that poor!", "good"))
# else:
#     print(x)

# 015

# def longestLength(a):
#     long = len(a[0])
#     temp = a[0]
    
#     for i in a:
#         if (len(i)> long):
#             long = len(i)
#             temp = i
#     print(f"The word with longest length is {temp} and the length is {long}")

# a = input("Enter words: ").split(",")
# longestLength(a)

# 016

# z = input("Enter anything: ")
# for i in z:
#     print(z.isdigit())

# 017
# import operator

# a = {'a': 12, 'b': 5, 'c': 89, 'd': 34}

# print("Original dictionary: ", a, "\n")

# sorted_a = sorted(a.items(), key= operator.itemgetter(1))
# print("Dictionary in ascending order by value: ",sorted_a, "\n")

# sorted_a = sorted(a.items(), key= operator.itemgetter(1), reverse=True)
# print("Dictionary in Descending order by value: ",sorted_a)

# 018 

# a = {12: 'a', 5: 'b', 45: 'c', 76: 'd', 0: 'e'}
# a = {'c': 12, 'd': 5, 'a': 89, 'b': 34}
# l = list(a.items())
# l.sort()
# dict = dict(l)
# print("Dictionary in ascending order by value: ", l)

# l = list(a.items())
# l.sort(reverse=True)
# print("Dictionary in Descending order by value: ",l)

# 019
# a = {0: 10, 1: 20}
# print("Original dict is: ", a)

# a[2] = 30
# a.update({3: 40})

# print("New dict is: ", a)

# 020
def merge_dict(dict1, dict2, dict3):
    x = (dict2.update(dict1))
    y = (dict3.update(dict2))
    return y
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}

print(merge_dict(dict1, dict2, dict3))
print(dict3)