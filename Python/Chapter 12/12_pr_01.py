def findFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"file {filename} not found")
        
findFile("1.txt")
findFile("2.txt")
findFile("3.txt")