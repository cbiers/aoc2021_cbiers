def maxX(d):
    res = 0
    for dx in d:
        res = max([res, dx[0], dx[2]])
    return res

def maxY(d):
    res = 0
    for dy in d:
        res = max([res, dy[1], dy[3]])
    return res

def count(c):
    count = 0
    for line in c:
        for d in line:
            if(d > 1):
                count += 1
    return count

f = open("in.txt", "r")
lines = f.readlines()

data = []

for line in lines:
    sep = line.find("-")
    p1 = line[:sep-1].split(",")
    p2 = line[sep+3:].split(",")
    data.append([int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1][:-1])])

maxY = maxY(data)

counter = []
for i in range(maxX(data)+1):
    counter.append([0 for i in range(maxY+1)])

for d in data:
    if d[0] == d[2]:
        if d[1] < d[3]:
            for i in range(d[1], d[3]+1):
                counter[d[0]][i] += 1
        else:
            for i in range(d[3], d[1]+1):
                counter[d[0]][i] += 1
    elif d[1] == d[3]:
        if d[0] < d[2]:
            for i in range(d[0], d[2]+1):
                counter[i][d[1]] += 1
        else:
            for i in range(d[2], d[0]+1):
                counter[i][d[1]] += 1
    elif d[0] < d[2]:
        if d[1] < d[3]:
            pos = 0
            for i in range(d[0], d[2]+1):
                counter[i][d[1]+pos] += 1
                pos += 1
        else:
            pos = 0
            for i in range(d[0], d[2]+1):
                counter[i][d[1]-pos] += 1
                pos += 1
    else:
        if d[1] < d[3]:
            pos = 0
            for i in range(d[2], d[0]+1):
                counter[i][d[3]-pos] += 1
                pos += 1
        else:
            pos = 0
            for i in range(d[2], d[0]+1):
                counter[i][d[3]+pos] += 1
                pos += 1

print count(counter)
