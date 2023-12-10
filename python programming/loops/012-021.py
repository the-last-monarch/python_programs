#012
# lines = []
# while True:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else:
#         break;
    
# for l in lines:
#     print(l)


#013
# items = []
# num = [x for x in  input("Enter 4 digit binary number:").split(',')]

# for a in num:
#     x = int(a, 2)
#     if not x% 5:
#         items.append(a)
# print(','.join(items))


#014
# a = input("Enter string: ")
# ## l = Letters
# ## d = Digits
# d = 0
# l = 0
# for x in a:
#     if x.isdigit():
#         d = d + 1
#     elif x.isalpha():
#         l = l + 1
#     else:
#         pass
# print(l)
# print(d)


#015
# import re
# x = input("Enter password:\n")
# s = True
# while s:
#     if (len(x)<6 or len(x)>12):
#         print("You password is too short or maybe too long")
#         break
#     elif not re.search("[a-z]", x):
#         print("You forget [a-z]")
#         break
#     elif not re.search("[A-Z]", x):
#         print("You forget [A-Z]")
#         break
#         #SHADOW
#     elif not re.search("[0-9]", x):
#         print("You forget [0-9]")
#         break
#     elif not re.search("[!@#$]", x):
#         print("You forget [!$#@]")
#         break
#     elif not re.search("[\s]", x):
#         print("You forget space")
#         break
#     else:
#         print("Valid Password")
#         print(f"Your password is:", x)
#         s = False
#         break
# if s:
#     print("Not a valid password")


#016
# num = []
# for n in range(100,401):
#     s = str(n) 
#     if (int(s[0])%2 == 0) and (int(s[1])%2 == 0) and (int(s[2])%2 == 0):
#         num.append(s)
# print(",".join(num))


#017
# result_str = ""
# for row in range(0,7):
#     for column in range(0,6):
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "
#             #SHADOW
#     result_str = result_str + "\n"
# print(result_str)


#018
# result_str = ""
# for row in range (0, 7):
#     for column in range(0, 7):
#         if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "
#     result_str = result_str + "\n"
# print(result_str)


#019
# result_str = ""
# for row in range(0,7):
#     for column in range (0,7):
#         # if (row == 0 or row == 3 or row == 6) or (column == 0 or column == 5 and (row != 0 and row != 3 and row != 6)):
#         if (column == 1 or (row == 0 or row == 6) and (column > 1 and column < 7)) or (row == 3 and (column > 1 and column < 6)):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + ""
#     result_str = result_str + "\n"
# print(result_str)


#020
# result_str = ""
# for row in range(0,7):
#     for column in range(0,7):
#         if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "
#     result_str = result_str + "\n"
# print(result_str)


#021
# result_str = ""
# for row in range(0,7):
#     for column in range(7):
#         if (column == 1 or (row == 6 and column != 0)):
#             result_str=result_str+"*"
#         else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str)
