m1 = int(input("Enter marks of 1st test: "))
m2 = int(input("Enter marks of 2nd test: "))
m3 = int(input("Enter marks of 3rd test: "))

if m1 > m2:
    if m2 > m3:
        total = m1 + m2
    else:
        total = m1 + m3
elif m1 > m3:
    total = m1 + m2
else:
    total = m2 + m3

avg = total/2
print("Average of all tests", avg)