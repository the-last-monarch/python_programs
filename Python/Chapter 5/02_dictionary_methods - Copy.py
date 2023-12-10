myDict = {
            "shadow": "something black in colour behind your body when you are under any light",
            "colour":  "any thing which we can see",
            "vs code": "a place of typing",
            "numbers": [1, 2 ,3 ,4],
            "ekordict": {"colour": 'red'}
}

# Dictionary methods
# print(list(myDict.keys())) # prints the keys of the dictionary
# print(myDict.values())
# print(myDict.items()) #print the (keys, values) of the dictionary 
# print(myDict)
updatedict = {
        "hero": "who always wins in the end",
        "numbers": [23, 43, 78], #this change actual value if the key is already in the dictionary (like in row 5)
}
(myDict.update(updatedict)) # update the dictionary by adding key/value pairs from the updatedict
# print(myDict)

# shows the diffirence betwen .get and [] syntex in the dictionaries. 
print(myDict.get("shadow")) # Print value assiosated with key "shadow"
print(myDict.get("shadow2")) # print None ass shadow2 is not in dictionary

print(myDict["shadow"]) # Returns with value assiosated with key "shadow"
print(myDict["shadow2"]) # throws an error that shadow2 is not in dicitionary
