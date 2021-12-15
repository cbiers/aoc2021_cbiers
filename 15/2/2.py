def smallestCost(c, v, f):
    min = 1000000000000
    minX = -1
    minY = -1
    for (x, y) in fringe:
        if not v[x][y] and c[x][y] < min:
            min = costs[x][y]
            minX = x
            minY = y
    return (minX, minY)

def updateCost(g, c, x0, y0, x1, y1):
    newCost = c[x0][y0] + g[x1][y1]
    if newCost < c[x1][y1]:
        c[x1][y1] = newCost

def appendLine(g, l):
    newLine = []
    for i in range(5):
        for c in l:
            toAppend = int(c) + i
            if toAppend > 9:
                toAppend = toAppend - 9
            newLine.append(toAppend)
    g.append(newLine)

def repeatLines(g, res, offset):
    for line in g:
        newLine = []
        for c in line:
            toAppend = c + offset
            if toAppend > 9:
                toAppend = toAppend - 9
            newLine.append(toAppend)
        res.append(newLine)


f = open("in.txt", "r")
lines = f.readlines()

grid = []

for line in lines:
    appendLine(grid, line[:-1])

curr = grid[:]

for offset in range(1, 5):
    repeatLines(curr, grid, offset)

visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
costs = [[1000000000000 for j in range(len(grid[0]))] for i in range(len(grid))]
costs[0][0] = 0

fringe = [(0, 0)]

while fringe:
    (i, j) = smallestCost(costs, visited, fringe)
    if (i, j) == (len(grid)-1, len(grid[0])-1):
        print costs[i][j]
        break
    print str(numVis) + "/" + str(tot)
    if i != len(grid)-1 and not visited[i+1][j]:
        fringe.append((i+1, j))
        updateCost(grid, costs, i, j, i+1, j)
    if j != len(grid[0])-1 and not visited[i][j+1]:
        fringe.append((i, j+1))
        updateCost(grid, costs, i, j, i, j+1)
    if i != 0 and not visited[i-1][j]:
        fringe.append((i-1, j))
        updateCost(grid, costs, i, j, i-1, j)
    if j != 0 and not visited[i][j-1]:
        fringe.append((i, j-1))
        updateCost(grid, costs, i, j, i, j-1)
