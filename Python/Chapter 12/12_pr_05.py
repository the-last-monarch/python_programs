num = int(input("Enter the number: "))

table = [num*i for i in range(1,11)]
with open('table.txt', 'a') as f:
    f.write(str(table))
    f.write('\n')
print(table)