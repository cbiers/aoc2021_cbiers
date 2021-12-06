f = open("in.txt", "r")
lines = f.readlines()[0][:-1]
vals = [int(x) for x in lines.split(",")]

for i in range(256):
    append = 0
    for i in range(len(vals)):
        if vals[i] == 0:
            vals[i] = 6
            append += 1
        else:
            vals[i] -= 1
    for i in range(append):
        vals.append(8)

print len(vals)
