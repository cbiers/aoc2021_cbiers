def getPathsRec(conns, curr, path, visits):
    if curr == "end":
        return 1
    path.append(curr)
    if curr.islower():
        visits[curr] += 1
    paths = 0
    for conn in conns[curr]:
        if conn != "start" and not (conn.islower() and visits[conn] >= 1 and 2 in visits.values()):
            paths += getPathsRec(conns, conn, path[:], visits.copy())
    return paths

def getPaths(conns, curr):
    visits = {}
    for conn in conns.keys():
        if conn.islower():
            visits[conn] = 0
    return getPathsRec(conns, curr, [], visits)

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
