import functools

f = open("in.txt", "r")
lines = f.readlines()[0][:-1]
vals = [int(x) for x in lines.split(",")]

counters = [0 for i in range(9)]

for i in vals:
    counters[i] += 1

for i in range(256):
    temp = counters[0]
    for i in range(8):
        counters[i] = counters[i + 1]
    counters[6] += temp
    counters[8] = temp

print functools.reduce(lambda a,b: a + b, counters)
