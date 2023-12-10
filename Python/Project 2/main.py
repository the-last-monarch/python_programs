import random
randNumber = random.randint(1,100)
user = None
guessed = 0

while (user != randNumber):
    user = int(input("Enter your number: "))
    guessed += 1
    if user==randNumber:
        print("Congratulations, you guess right number")
    else:
        if user>randNumber: 
            print("Saddly, you guessed wrong number, guess a smaller number")
        else:
            print("Saddly, you guessed wrong number, guess a higher number")
    
    
print(f"You have guessed number in {guessed} times")

with open('hiscore.txt') as f:
    hiscore = int(f.read())
    
if (guessed<hiscore):
    print("Superb, Congratulations you just break previous high score.")
    with open('hiscore.txt', 'w') as f:
        f.write(str(guessed))