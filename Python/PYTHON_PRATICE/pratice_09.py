num = int(input("Enter the number: "))
count = 5
for i in range(0,num+1):
    for j in range(count-i,0,-1):
        print(j,end='')
    print()