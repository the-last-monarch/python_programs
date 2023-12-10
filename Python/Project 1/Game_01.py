import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(Computer,You ):
    # If two values are equal, declare a tie!
    #SHADOW
    if Computer == You:
        return None
    
    # Check for all possibilities when computer chose s
    elif Computer == 's':
        if You == 'w':
            return False
        elif You == 'g':
            return True
        
    # Check for all possibilities when computer chose w
    elif Computer == 'w':
        if You == 'g':
            return False
        elif You == 's':
            return True   
        
    # Check for all possibilities when computer chose g     
    elif Computer == 'g':
        if You == 's':
            return False
        elif You == 'w':
            return True

print("Comp turn: Snake(s), Water(w), Gun(g)?")
randomNo = random.randint(1, 3)
if randomNo == 1:
    Computer = 's'
elif randomNo == 2:
    Computer = 'w'
elif randomNo == 3:
    Computer = 'g'
    
You = input("Your's turn: Snake(s), Water(w), Gun(g) ")
a = gameWin(Computer, You)

print(f"Computer choose {Computer}")
print(f"You choose {You}")

if a == None:
    print("This match is a tie!")
elif a == False:
    print("You lose this round!")
else:
    print("You win!")