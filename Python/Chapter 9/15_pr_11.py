import os

old_name = "hiscore.txt"
new_name = "renamed_by_python.txt"

with open(old_name) as f:
    content = f.read()
    
with open(new_name, 'w') as f:
    f.write(content)
    
os.remove(old_name)