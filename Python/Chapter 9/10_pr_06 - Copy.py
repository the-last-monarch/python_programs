with open("log.txt")as f:
    content = f.read()
    
# Use .lower() to find any word with lower case if it in present in upper case(you can use it as f.read().lower() in line 2)
if "python" in content.lower():
    print("Yes there is python in  file.")
else:
    print("Sorry, there is no file named 'python'")