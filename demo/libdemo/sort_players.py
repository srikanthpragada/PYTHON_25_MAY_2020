from datetime import datetime

with  open("players.txt", "rt") as f:
    players = {}
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue

        name = parts[0]
        dobstr = parts[1]
        dob = datetime.strptime(dobstr, "%Y-%m-%d")
        age = (datetime.now() - dob).days // 365
        players[name] = age

for name, age in sorted(players.items(), key=lambda t: t[1]):
    print(f"{name:20}  {age:2}")
