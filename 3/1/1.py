f = open("in.txt", "r")
lines = f.readlines()

zero = [0 for i in range(len(lines[0]) - 1)]

for line in lines:
    for i in range(len(line) - 1):
        if line[i] == "0":
            zero[i] += 1

epsilon = ""
gamma = ""

for bin in zero:
    if bin > len(lines) / 2:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

epsdec = int(epsilon, 2)
gamdec = int(gamma, 2)

res = epsdec * gamdec

print res
