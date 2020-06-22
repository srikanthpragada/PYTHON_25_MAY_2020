with open("students.txt", "rt") as f:
    students = {}
    for line in f.readlines():
        if len(line.strip()) == 0:  # blank line
            continue

        parts = line.split(",")
        name = parts[0]
        marks = parts[1:]  # Second element onwards
        total = sum(map(int, marks))
        students[name] = total

    for (name, total) in sorted(students.items()):
        print(f"{name:15} {total:3}")
