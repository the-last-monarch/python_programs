def number(num):
    try:
        return int(num)+1
    except:
        raise ValueError ("This is not a number")
num = number('das43')
print(num)