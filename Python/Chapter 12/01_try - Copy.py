while (True):
    print("Press q to quit the game")
    a = input("Enter the number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a<10:
            print("Enter a number greater than 10")
    except Exception as e:
        print(f"I told to enter only number not anything that comes in your mind ({e})")
        
print("If you enjoy then come again anytime you want")