import random
def GameRank(Computer, You):
    
    if Computer == You:
        return None
    
    
    elif Computer == 's':
        if You == 'w':
            return False
        elif You == 'g':
            return True
        
        
    elif Computer == 'w':
        if You == 'g':
            return  False
        if You == 's':
            return True
        
    elif Computer == 'g':
        if You == 's':
            return False
        if You == 'w':
            return True


print("Computer's turn = Snake(s), Water(w), gun(g)")

RandomNumber = random.randint(1,3)

if RandomNumber == 1:
    Computer = 's'
    
elif RandomNumber == 2:
    Computer = 'w'
    
elif RandomNumber == 3:
    Computer = 'g'

You = input("Your turn = Snake(s), Water(w), gun(g)\n")

a = GameRank(Computer, You)

print(f"Computer choose {Computer}")
print(f"You choose {You}")

if a == None:
    print("This match is a tie!")
elif a == False:
    print("You lose this match!")
else:
    print("You win!")