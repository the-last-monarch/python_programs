comment = input("Enter you comment\n")

if("click this" in comment):
    spam = True
elif("subscribe this" in comment):
    spam = True
elif("buy now" in comment):
    spam = True
elif("make lot of money" in comment):
    spam = True
else:
    spam = False

if(spam):
    print("THIS COMMENT IS SPAM")
else:
    print("THIS COMMENT IS NOT A SPAM")