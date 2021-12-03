f = open("in.txt", "r")
lines = f.readlines()

curr = int(lines[0])
count = 0

for line in lines[1:]:
    if int(line) > curr:
        count += 1
    curr = int(line)

print(count)
