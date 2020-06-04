
data = "101:90,103:60,104:70,102:95,106:86"

parts = data.split(",")

students = {}
for value in parts:
    rollno, marks = value.split(':')
    students[rollno] = marks


for rollno, marks in sorted(students.items()):
    print(rollno,marks)

