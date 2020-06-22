with open("names.txt", "rt") as f:  # Write text
    for name in sorted(f.readlines()):
        print(name.strip())
