#001
# import math

# class circle:
    
#     # Initialize the Circle object with a given radius
#     def __init__(self, radius):
#         self.radius = radius
        
#     # Calculate and return the area of the circle using the formula: π * r^2
#     def area_of_circle(self):
#         return math.pi * self.radius**2
    
#     # Calculate and return the perimeter (circumference) of the circle using the formula: 2π * r
#     def perimeter_of_circle(self):
#         return 2 * math.pi * self.radius

# # Prompt the user to input the radius of the circle and convert it to a floating-point number
# radius = float(input("Enter radius of circle: "))

# # Create a Circle object with the provided radius
# circle = circle(radius)

# area = circle.area_of_circle()
# perimeter = circle.perimeter_of_circle()

# print("area of circle is", area)
# print("perimeter of circle is", perimeter)


#002
# from datetime import date

# class person:
#     def __init__(self, name, country, dob):
#         self.name = name
#         self.country = country
#         self.dob = dob
        
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.dob.year
#         if today < date(today.year, self.dob.month, self.dob.day):
#             age -= 1
#         return age
    
# person1 = person("shadow", "france", date(1967, 7, 12))

# print("Person1 :-")
# print("Name:", person1.name)
# print("Country:", person1.country)
# print("DOB:", person1.dob)
# print("age:", person1.calculate_age())


#003
# class calculator:
    
#     def addition(self, x, y):
#         return x + y
    
#     def subtract(self, x, y):
#         return x - y
    
#     def multiply(self, x, y):
#         return x * y
    
#     def divide(self, x, y):
#         if y != 0:
#             return x / y
#         else:
#             return("Can't divide by zero")

# calculator = calculator()

# print('''1) To add enter 1
# 2) To subtract enter 2
# 3) To multiply enter 3
# 4) To divide enter 4''')
# #SHADOW

# entry = int(input("Enter your choice: "))

# if entry == 1:
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))

#     result_add = calculator.addition(x, y)
#     print("result of", x, "+", y, "=", result_add)
    
# elif entry == 2:
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))

#     result_sub = calculator.subtract(x, y)
#     print("result of", x, "-", y, "=", result_sub)
    
# elif entry == 3:
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))

#     result_multiply = calculator.multiply(x, y)
#     print("result of", x, "*", y, "=", result_multiply)
    
# elif entry == 4:
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))

#     result_divide = calculator.divide(x, y)
#     print("result of", x, "/", y, "=", result_divide)

# else:
#     print("This is calculator not your notepad ONLY ENTER GIVEN CHOICES.")


#004
import math
class shapes:
    pass