f = open("in.txt", "r")
lines = f.readlines()

count = 0

for i in range(1, len(lines) - 2):
    sum = reduce(lambda a, b: int(a) + int(b), lines[i-1:i+2])
    sum2 = reduce(lambda a, b: int(a) + int(b), lines[i:i+3])
    if sum2 > sum:
        count += 1

print(count)
