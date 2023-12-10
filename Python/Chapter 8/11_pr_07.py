def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

a = "      Who are you dead          "
n = remove_and_split(a, "dead")
print(n)