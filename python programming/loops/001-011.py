#001
# x = []
# m = int(input("Enter First number: "))
# n = int(input("Enter Second number: "))
# for a in range(m,n):
#     if (a%7==0) and (a%5==0):
#         x.append(str(a))
# print(','.join(x))

# 002
# temp = input("Enter any value of temprature you want to convert.(e.g., 35F, 107C etc.)")
# degree = int(temp[:-1])
# i_convertion = temp[-1]

# if i_convertion.upper() == "C":
#     result = int(round((9 * degree)/5 + 32))
#     o_convertion = "Fehrenheit"
# elif i_convertion.upper() == "F":
#     result = int(round((degree - 32)*5/9))
#     o_convertion = "Celsius"
# else:
#     print("Invalid Entry.")
#     quit()
# print(f"The tempature in", o_convertion,"is", result,"degree.")

# print(degree)
# print(i_convertion)

#003
# import random
# # target_num = random.randint(1,10)
# # guess_num = 0
# target_num, guess_num = random.randint(1,10), 0
# # both of above code will work similar
# while target_num != guess_num:
#     guess_num = int(input("Guess any number between 1 to 9 = "))
# print("Well guessed")

#004
# n = int(input("How many stars you want to see: "))
# for i in range(n):
#     for j in range(i):
#         print('*', end="")
#     print('')
#        #SHADOW
# for i in range(n,0,-1):
#     for j in range (i):
#         print('*', end="")
#     print('')

#005
# word = input("Enter word you want to do reverse: ")
# for char in range(len(word) -1,-1,-1):
#     print(word[char], end="")
# print("\n")

#006
# numbers = (1,2,3,4,5,6,7,8,9)
# count_odd = 0
# count_even = 0
# for x in numbers:
#     if not x % 2:
#         count_even += 1 
#     else:
#         count_odd += 1
# print(f"Number of even numbers: ", count_even)
# print(f"Number of odd numbers: ", count_odd)

# # enter = tuple(input("Anything: "))
# # print(type(enter))

#007
# datalist = [123, 11.22, 1+2j, True, "Shadow", (0,-1), [2,3], {"section:A", "section:B"}]

# for item in datalist:
#     print(f"Type of", item, "is", type(item))

#008
# for i in range(6):
#     if (i == 3 or i == 6):
#         continue
#     print(i,end=" ")
# print("\n")

# 009 
# # type 1
# # n = int(input("Enter number how long you want this Fibonacci series:"))
# # num1 = 0
# # num2 = 1
# # next_num = num2
# # count = 1

# # while count <= n:
# #     print(next_num, end=" ")
# #     count += 1
# #     num1, num2 = num2, next_num
# #     next_num = num1 + num2
#     SHADOW
# # print()

# # type 2
# # x = 0
# # y = 1

# # while y < 50:
# #     print(y)
# #     x, y = y,x+y

#010
# for FizzBuzz in range (51):
#     # if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
#     #     print("FizzBuzz")
#         # continue
#     if FizzBuzz % 3 == 0:
#         print("Fizz")
#         continue
#     elif FizzBuzz % 5 == 0:
#         print("Buzz")
#         continue
#     print(FizzBuzz)

# 011
# ?
# ?
# ?
# ?
# ?
# ?