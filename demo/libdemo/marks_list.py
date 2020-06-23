with open("students.txt", "rt") as f:
    students = {}
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:  # blank line
            continue

        parts = line.split(",")
        if len(parts) > 1:
            name = parts[0]
            marks = parts[1:]  # Second element onwards
            try:
               total = sum(map(int, marks))
               students[name] = total
            except:
                pass


    for (name, total) in sorted(students.items()):
        print(f"{name:15} {total:3}")
