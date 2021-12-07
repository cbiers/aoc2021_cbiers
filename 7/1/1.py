f = open("in.txt", "r")
lines = f.readlines()[0][:-1]
vals = [int(x) for x in lines.split(",")]

minVal = min(vals)
maxVal = max(vals)

bestVal = -1

for val in vals:
    sum = 0
    for val2 in vals:
        sum += abs(val2 - val)
    if sum < bestVal or bestVal == -1:
        bestVal = sum

print bestVal
