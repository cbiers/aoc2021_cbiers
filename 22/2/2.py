def split(e, c):
    

def overlap(e1, e2):
    xOver = e1["xMin"] <= e2["xMin"] and e2["xMin"] <= e1["xMax"] or e2["xMin"] <= e1["xMin"] and e1["xMin"] <= e2["xMax"]
    yOver = e1["yMin"] <= e2["yMin"] and e2["yMin"] <= e1["yMax"] or e2["yMin"] <= e1["yMin"] and e1["yMin"] <= e2["yMax"]
    zOver = e1["zMin"] <= e2["zMin"] and e2["zMin"] <= e1["zMax"] or e2["zMin"] <= e1["zMin"] and e1["zMin"] <= e2["zMax"]
    return xOver and yOver and zOver

def addToWorld(w, c):
    toRemove = []
    toAdd = []
    for e in w:
        if overlap(e, c):
            toRemove.append(e)
            toAdd.append(split(e, c))
    w.append(c)
    for r in toRemove:
        w.remove(r)
    for a in toAdd:
        for c in a:
            w.append(a)

def countCubes(w):
    count = 0
    for cube in w:
        xLen = cube["xMax"] - cube["xMin"] + 1
        yLen = cube["yMax"] - cube["yMin"] + 1
        zLen = cube["zMax"] - cube["zMin"] + 1
        count += xLen * yLen * zLen

f = open("in.txt", "r")
lines = f.readlines()

cubes = []
instructions = []

for line in lines:
    cube = {}
    if line[1] == "n":
        instructions.append(True)
        coords = line[3:]
    else:
        inst["on"] = False
        coords = line[4:]
    coords = coords.split(",");
    cube["xMin"] = coords[0].split("..")[0][2:]
    cube["xMax"] = coords[0].split("..")[1]
    cube["yMin"] = coords[1].split("..")[0][2:]
    cube["yMax"] = coords[1].split("..")[1]
    cube["zMin"] = coords[2].split("..")[0][2:]
    cube["zMax"] = coords[2].split("..")[1][:-1]
    cubes.append(cube)

world = []

for i in range(len(cubes)):
    cube = cubes[i]
    if instructions[i]:
        addToWorld(world, cube)
    else:
        removeFromWorld(world, cube)

print countCubes(world)
