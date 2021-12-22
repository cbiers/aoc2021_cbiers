def countOn(s):
    count = 0
    for i in range(len(s)):
        for j in range(len(s[0])):
            for k in range(len(s[0][0])):
                if s[i][j][k]:
                    count += 1
    return count

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
        instructions.append(False)
        coords = line[4:]
    coords = coords.split(",");
    cube["xMin"] = int(coords[0].split("..")[0][2:])
    cube["xMax"] = int(coords[0].split("..")[1])
    cube["yMin"] = int(coords[1].split("..")[0][2:])
    cube["yMax"] = int(coords[1].split("..")[1])
    cube["zMin"] = int(coords[2].split("..")[0][2:])
    cube["zMax"] = int(coords[2].split("..")[1][:-1])
    cubes.append(cube)

state = [[[False for i in range(-50, 51)] for j in range(-50, 51)] for k in range(-50, 51)]

for i in range(len(cubes)):
    xMin = cubes[i]["xMin"] + 50
    xMax = cubes[i]["xMax"] + 50
    yMin = cubes[i]["yMin"] + 50
    yMax = cubes[i]["yMax"] + 50
    zMin = cubes[i]["zMin"] + 50
    zMax = cubes[i]["zMax"] + 50
    if xMin >= 0 and xMax <= 100 and yMin >= 0 and yMax <= 100 and zMin >= 0 and zMax <= 100:
        for j in range(xMin, xMax+1):
            for k in range(yMin, yMax+1):
                for l in range(zMin, zMax+1):
                    state[j][k][l] = instructions[i]

print countOn(state)
