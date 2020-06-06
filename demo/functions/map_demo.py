nums = ["10", "20", "100", "50", "25"]


for n in nums:
    print(n)

for n in map(int,nums):
    print(n)

print(sum(map(int,nums)))