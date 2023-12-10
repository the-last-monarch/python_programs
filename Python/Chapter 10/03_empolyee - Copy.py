class empolyee:
    company = "Google"
    salary = 100
    
Shadow = empolyee()
Dead = empolyee()
Shadow.salary = "50k"
Dead.salary = "30k"
print(Shadow.company)
print(Dead.company)

empolyee.company = "Youtube"

print(Shadow.company)
print(Dead.company)
print(Shadow.salary)
print(Dead.salary)
