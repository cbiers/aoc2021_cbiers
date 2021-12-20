f = open("in.txt", "r")
lines = f.readlines()

probes = [[]]
curr = 0

for line in lines[1:]:
    if line[0] == "\n":
        continue
    if line[0:2] == "--":
        curr += 1
        probes.append([])
        continue
    probes[curr].append([int(i) for i in line[:-1].split(",")])
