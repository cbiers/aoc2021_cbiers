def appendAll(l, l2):
    for el in l2:
        if el not in l:
            l.append(el)
    return l

def genBassinRec(data, i, j, l):
    if data[i][j] != 9:
        l.append((i, j))
        if (i-1, j) not in l and i != 0 and data[i-1][j] > data[i][j]:
            appendAll(l,genBassinRec(data, i-1, j, l))
        if (i, j-1) not in l and j != 0 and data[i][j-1] > data[i][j]:
            appendAll(l, genBassinRec(data, i, j-1, l))
        if (i, j+1) not in l and j != len(data[i])-1 and data[i][j+1] > data[i][j]:
            appendAll(l, genBassinRec(data, i, j+1, l))
        if (i+1, j) not in l and i != len(data)-1 and data[i+1][j] > data[i][j]:
            appendAll(l, genBassinRec(data, i+1, j, l))
    return l

def genBassin(data, i, j):
    return genBassinRec(data, i, j, [])

f = open("in.txt", "r")
lines = f.readlines()
data = []
for line in lines:
    data.append([int(x) for x in line[:-1]])

bassins = []

for i in range(len(data)):
    for j in range(len(data[i])):
        if i != 0 and data[i-1][j] <= data[i][j]:
            continue
        if j != 0 and data[i][j-1] <= data[i][j]:
            continue
        if j != len(data[i])-1 and data[i][j+1] <= data[i][j]:
            continue
        if i != len(data)-1 and data[i+1][j] <= data[i][j]:
            continue
        bassins.append(genBassin(data, i, j))

bassins.sort(key=len)

print len(bassins[-1]) * len(bassins[-2]) * len(bassins[-3])
