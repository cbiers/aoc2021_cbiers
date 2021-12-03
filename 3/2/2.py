f = open("in.txt", "r")
lines = f.readlines()

index = 0

while len(lines) > 1:
    lines2 = []
    zero = 0
    one = 0
    for i in range(len(lines)):
        if lines[i][index] == "0":
            zero += 1
        else:
            one += 1
    for line in lines:
        if not((zero > one and line[index] == "1") or (zero <= one and line[index] == "0")):
            lines2.append(line)
    index += 1
    lines = lines2

oxy = lines[0]

f = open("in.txt", "r")
lines = f.readlines()

index = 0

while len(lines) > 1:
    lines2 = []
    zero = 0
    one = 0
    for i in range(len(lines)):
        if lines[i][index] == "0":
            zero += 1
        else:
            one += 1
    for line in lines:
        if not((zero > one and line[index] == "0") or (zero <= one and line[index] == "1")):
            lines2.append(line)
    index += 1
    lines = lines2

co2 = lines[0]

oxydec = int(oxy, 2)
co2dec = int(co2, 2)

res = oxydec * co2dec

print res
