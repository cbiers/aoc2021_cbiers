def foldX(points, val):
    toDelete = []
    for i in range(len(points)):
        point = points[i]
        if point[0] > val:
            newPoint = [val - (point[0] - val), point[1]]
            if newPoint not in points:
                points.append(newPoint)
            toDelete.append(i)
    toDelete.sort(reverse=True)
    for i in toDelete:
        points.pop(i)

def foldY(points, val):
    toDelete = []
    for i in range(len(points)):
        point = points[i]
        if point[1] > val:
            newPoint = [point[0], val - (point[1] - val)]
            if newPoint not in points:
                points.append(newPoint)
            toDelete.append(i)
    toDelete.sort(reverse=True)
    for i in toDelete:
        points.pop(i)

f = open("in.txt", "r")
lines = f.readlines()

part = 1
points = []
folds = []

for line in lines:
    if not line.strip():
        part = 2
        continue
    if part == 1:
        points.append([int(x) for x in line.split(",")])
    else:
        fold = line[11:].split("=")
        folds.append({"axis": fold[0], "val": int(fold[1])})

for fold in folds:
    if fold["axis"] == "x":
        foldX(points, fold["val"])
    else:
        foldY(points, fold["val"])

maxX = 0
maxY = 0

for point in points:
    if point[0] > maxX:
        maxX = point[0]
    if point[1] > maxY:
        maxY = point[1]

for i in range(maxY+1):
    s = ""
    for j in range(maxX+1):
        if [j, i] in points:
            s += "#"
        else:
            s += "."
    print s
