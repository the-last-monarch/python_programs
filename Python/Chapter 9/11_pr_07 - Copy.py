content = True
i = 1

with open("log.txt")as f:
    while content:
        content = f.readline()
        if "python" in content.lower():
            print(content)
            print(f"Yes there is python in  file.And it is present in line no.{i}")
        i+=1
