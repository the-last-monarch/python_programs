def game():
    return 56 

score = game()
with open('C:\\Users\\Monty Grewal\\Documents\\Python\\hiscore.txt') as f:
    hiscore = f.read()
    
if hiscore=='':
    with open('C:\\Users\\Monty Grewal\\Documents\\Python\\hiscore.txt', 'w') as f:
        f.write(str(score))
        
elif int(hiscore)<score:
    with open('C:\\Users\\Monty Grewal\\Documents\\Python\\hiscore.txt', 'w') as f:
        f.write(str(score))