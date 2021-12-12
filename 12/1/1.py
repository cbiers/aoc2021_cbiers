def getPathsRec(conns, curr, path):
    if curr == "end":
        return 1
    path.append(curr)
    paths = 0
    for conn in conns[curr]:
        if conn != "start" and not (conn.islower() and conn in path):
            paths += getPathsRec(conns, conn, path[:])
    return paths

def getPaths(conns, curr):
    return getPathsRec(conns, curr, [])

f = open("in.txt", "r")
lines = f.readlines()

conns = {}

for line in lines:
    a = line.split("-")[0]
    b = line.split("-")[1][:-1]
    if a not in conns.keys():
        conns[a] = []
    if b not in conns.keys():
        conns[b] = []
    conns[a].append(b)
    conns[b].append(a)

print getPaths(conns, "start")
