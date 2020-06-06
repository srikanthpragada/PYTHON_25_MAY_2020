data = "101:90,103:60,104:70,101:80,102:80,102:95,106:86,108,103:90"

students = {}

for part in data.split(","):
    if ':' not in part:
        continue

    rollno, marks = part.split(":")
    if rollno in students:
        students[rollno].append(marks)
    else:
        students[rollno] = [marks]

for rollno, marks in sorted(students.items()):
    print(rollno, ",".join(marks))

for rollno, marks in sorted(students.items()):
    print(rollno, sum(map(int, marks)))
