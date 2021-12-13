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

print len(points)

for fold in folds[:]:
    if fold["axis"] == "x":
        foldX(points, fold["val"])
    else:
        foldY(points, fold["val"])

print len(points)
