import os

walk_generator = os.walk(r"c:\classroom\may25")

for (name, folders, files) in walk_generator:
    for file in files:
        if file.endswith(".py"):
            print(name + "\\" + file)
