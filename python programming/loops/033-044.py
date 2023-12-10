#033

# print("Name of months", 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
# a =input("Enter month name to know dates in that month: ")

# if a in ("January", "March", "May", "July","August", "October", "December"):
#     print(f"Numbers of days in {a} month is 31 days" )
    
# elif a in ("February"):
#     print("In February there are 28/29 days")
    
# elif a in ("April", "June", "September", "November"):
#     print(f"In {a} there are 30 days")
    
# else:
#     print("Wrong month name")


#034
# a, b = [int(a) for a in input("Enter two integer: ").split(",")]
# if (a+b)>20:
#     print(a+b)
# else:
#     print(20)

#035
# enter = input("Enter a string: ")
# enter = enter.strip()
# if len(enter) < 1:
#     print("Enter valid text")
# else:
#     if all(enter[i] in "0123456789" for i in range(len(enter))):
#         print("This string is an integer")
#     elif (enter[0] in "+-") and \
#         all(enter[i] in "0123456789" for i in range(len(enter))):
#             print("This string is an string")
#     else:
#         print("This string is not an integer")


#036
# x, y, z = [int(x) for x in input("Enter x, y, z sides of triangle: ").split(",")]
# if x == y == z:
#     print("This is an equilateral")
# elif x != y == z:
#     print("This is isosceles")
# elif x == y != z:
#     print("This is isosceles")
# elif y != x == z:
#     print("This is isosceles")
# else:
#     print("This is scalene")


#037
# print("Name of months", 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
# a =input("Enter month name: ")
# b = int(input("Enter Date in above month: "))

# if a in ("January", "February", "March") or b == 3:
#     print("This is Winter Season")
    
# elif a in ("April", "May", "June") or b == 3:
#     print("This is Spring Season")
    
# elif a in ("July", "August", "September") or b == 3:
#     print("This is Summer Season")
    
# else:
#     print("This is Autumn Season")

# if (a == "March") >= 19:
#     print("This is Winter Season")

# elif (a == "June") > 20:
#     print("This is Winter Season")

# elif (a == "September") > 21:
#     print("This is Winter Season")

# elif (a == "December") > 20:
#     print("This is Winter Season")


#038
# a = int(input("Enter your Birth date: "))
# b = input("Enter your birth month: ").capitalize()

# if a > 31:
#     astro_sign = "STUPID!!!!"
#     print("Don't you know there are only 31 days in a month. Are you a stupid or you are using Calender on Aliens.") 

# elif b == "December":
#     astro_sign = "Sagittarius" if (a < 21) else "Capricorn"
    
# elif b == "January":
#     astro_sign = "Capricorn" if (a < 20) else "Aquarius"
    
# elif b == "February":
#     astro_sign = "Aquarius" if (a < 19) else "Pisces"
    
# elif b == "March":
#     astro_sign = "Pisces" if (a < 21) else "Aries"
    
# elif b == "April":
#     astro_sign = "Aries" if (a < 20) else "Taurus"
    
# elif b == "May":
#     astro_sign = "Taurus" if (a < 21) else "Gemini"
    
# elif b == "June":
#     astro_sign = "Gemini" if (a < 21) else "Cancer"
    
# elif b == "July":
#     astro_sign = "Cancer" if (a < 23) else "Leo"
    
# elif b == "Augest":
#     astro_sign = "Leo" if (a < 23) else "Virgo"
    
# elif b == "September":
#     astro_sign = "Virgo" if (a < 23) else "Libra"
    
# elif b == "October":
#     astro_sign = "Libra" if (a < 23) else "Scorpio"
    
# elif b == "November":
#     astro_sign = "Scorpio" if (a < 22) else "Sagittarius"

# print(f"Your Astrological Sign is {astro_sign}")


#39
# year = int(input("Enter your birth year: "))

# if (year - 2000) % 12 == 0:
#     sign = "Tiger"
    
# elif (year - 2000) % 12 == 1:
#     sign = 'Snake'
    
# elif (year - 2000) % 12 == 2:
#     sign = 'Horse'
    
# elif (year - 2000) % 12 == 3:
#     sign = 'sheep'
    
# elif (year - 2000) % 12 == 4:
#     sign = 'Monkey'
    
# elif (year - 2000) % 12 == 5:
#     sign = 'Rooster'
    
# elif (year - 2000) % 12 == 6:
#     sign = 'Dog'
    
# elif (year - 2000) % 12 == 7:
#     sign = 'Pig'
    
# elif (year - 2000) % 12 == 8:
#     sign = 'Rat'
    
# elif (year - 2000) % 12 == 9:
#     sign = 'Ox'
    
# elif (year - 2000) % 12 == 10:
#     sign = 'Tiger'
    
# else:
#     sign = 'Hare'

# print("Your Zodiac sign :",sign)


# 40
# # import statistics

# # x,y,z = [int(x) for x in input("Enter 3 numbers you want to find medium. etc(1,2,3): ").split(",")]

# # print(statistics.median([x,y,z]))

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if a > b:
#     if a < c:
#         medium = a
#     elif b > c:
#         medium = b
#     else:
#         medium = c
# else:
#     if a > c:
#         medium = a
#     elif b < c:
#         medium = b
#     else:
#         medium = c
# print("Medium is", medium)


#41
# year = int(input("Enter year: "))

# if (year % 400 == 0):
#     leap_year = True
# elif (year % 100 == 0):
#     leap_year = False 
# elif (year % 4 == 0):
#     leap_year = True
# else:
#     leap_year = False

# month = int(input("Enter month[1-12]: "))

# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30

# date = int(input("Enter date[1-31]: "))

# if date < month_length:
#     date += 1
# else:
#     date = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1

# print("Next date will be [date, month, year] %d-%d-%d." %(date, month, year))


#42
# print("Input some integers to calculate their sum and average. Input 0 to exit.")

# count = 0
# sum = 0.0
# number = 1

# while number != 0:
#     number = int(input(""))
#     sum = sum + number
#     count += 1
    
# if count == 0:
#     print("Enter some intergers or numbers")
# else:
#     print("Sum and Average of entered numbers,", {sum / (count - 1)}, {sum})
    
    
#43
# num = int(input("Enter number you want table: "))

# for i in range (1, 11):
#     print(num, "X", i, "=", num*i)


#44
# for i in range(10):
#     print(str(i) * i)