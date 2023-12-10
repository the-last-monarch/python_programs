sub1 = int(input("Marks of subject 1: "))
sub2 = int(input("Marks of subject 2: "))
sub3 = int(input("Marks of subject 3: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("you failed in exam due to less than 33% in one of the exam")
elif(sub1+sub2+sub3)/3<40:
    print("you fail in exam because due to less sum of all exam")
else:
    print("you pass")