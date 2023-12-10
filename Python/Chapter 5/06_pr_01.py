myDict = {
        "hava": "air",
        "aag" : "fire",
        "roshani": "light" 
}
print("opetions are", myDict.keys())
a = input("type your word here\n")

# print("This is meaning of your word" , myDict[a])

# below line won't throw an error if the word is not in dictionary
print("This is meaning of your word :" , myDict.get(a))
