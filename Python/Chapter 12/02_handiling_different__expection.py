a = True
while a<=100:
    try:
        a = int(input("Enter any number: "))
        b = 1/a
        c = print(b)
    except ValueError as e:
        print("Kya kar raha ha bhai")
    except ZeroDivisionError as e:
        print(f"kya gunda bana ga re tu")
    except TypeError as e:
        print("chal nikal pheli fursat me")
    