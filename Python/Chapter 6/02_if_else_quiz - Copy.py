from playsound import playsound
age = int(input("Enter you age\n"))
if(age>=18):
    print("yes")
else:
    playsound('kya gunda banage re tu.mp3')