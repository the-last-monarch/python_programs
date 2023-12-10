#022
# result_str = ""
# for row in range(7):
#     for column in range (7):
#         if ((column == 0 or column == 6) or (row == column and column>0 and column<4) or (column == 4 and row > 1 and row < 3) or (column == 5 and row > 0 and row < 2)):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "
#     result_str = result_str + "\n"
# print(result_str)


#023
# for row in range(7):
#     for column in range (7):
#         if(((column == 1 or column == 6) and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5)):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()


#024
# for row in range(7):
#     for column in range(6):
#         if((column == 1 or column == 5 and row > 0 and row < 3) or (row == 0 and column > 0 and column < 4)  or row == 3 and column > 0 and column < 4):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()


#025
# for row in range(7):
#     for column in range(7):
#         if((column == 1 or column == 5 and row > 0 and row < 3) or (row == 0 and column > 0 and column < 4)  or (row == 3 and column > 0 and column < 4) or row == column and row > 3):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()


#026
# for row in range(7):
#     for column in range(7):
#         if(((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or (column == 1 and (row == 1 or row == 2 or row == 6)) or (column == 5 and (row == 0 or row == 4 or row == 5))):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()



# row=16    
# col=18   
# result_str=""    
# for i in range(1,row):    
#     if((i<=3)or(i>=7 and i<=9)or(i>=13 and i<=15)):    
#         for j in range(1,col):    
#             result_str=result_str+"o"    
#         result_str=result_str+"\n"    
#     elif(i>=4 and i<=6):    
#         for j in range(1,5):
#             result_str=result_str+"o"    
#         result_str=result_str+"\n"    
#     else:    
#         for j in range(1,14):    
#             result_str=result_str+" "    
#         for j in range(1,5):    
#             result_str=result_str+"o"    
#         result_str=result_str+"\n"    
# print(result_str)


#027
# for row in range(7):
#     for column in range(7):
#         if (row == 0 or column == 3):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


#028
# for row in range(7):
#     for column in range(7):
#         if ((column == 0 or column == 6) and row != 6) or (row == 6 and column > 0 and column < 6):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


#029
# for row in range(7):
#     for column in range(7):
#         if((column == 1 or column == 5) and (row < 2 or row > 4) or row == column and column > 1 and column < 5 or (column == 2 and row == 4) or (column == 4 and row == 2)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


#030
# for row in range(7):
#     for column in range(7):
#         if(((row == 0 or row == 6) and column > 0 and column < 6) or row + column == 6):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


#031
# a = int(input("Enter human age: "))
# dog = ""
# if a < 0:
#     print("Age must be positive number")
#     exit()
# elif a <= 2:
#     dog = a * 10.5
# else:
#     dog = 21 + (a - 2) * 4
# print("Age of dog is", dog)


#032
# enter = input("Enter to check it vowel or constent: ")

# if enter in ("a","e","i","o","u"):
#     print("%s is a vowel"% enter)
# elif enter in ("y"):
#     print("Sometime Y consider as vowel and sometime consider as constent.")
# else:
#     print("%s is a constent."%enter)
# #SHADOW