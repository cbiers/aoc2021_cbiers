def notAllVisited(v):
    for i in range(len(v)):
        for j in range(len(v[0])):
            if v[i][j] == False:
                return True
    return False

def smallestCost(c, v):
    min = 1000000000000
    minX = -1
    minY = -1
    for i in range(len(costs)):
        for j in range(len(costs[0])):
            if not visited[i][j] and costs[i][j] < min:
                min = costs[i][j]
                minX = i
                minY = j
    return (minX, minY)

def updateCost(g, c, x0, y0, x1, y1):
    newCost = c[x0][y0] + g[x1][y1]
    if newCost < c[x1][y1]:
        c[x1][y1] = newCost

f = open("in.txt", "r")
lines = f.readlines()

grid = []

for line in lines:
    grid.append([int(x) for x in line[:-1]])

visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
costs = [[1000000000000 for j in range(len(grid[0]))] for i in range(len(grid))]
costs[0][0] = 0

while notAllVisited(visited):
    (i, j) = smallestCost(costs, visited)
    if (i, j) == (len(grid)-1, len(grid[0])-1):
        print costs[i][j]
        break
    visited[i][j] = True
    if i != len(grid)-1 and not visited[i+1][j]:
        updateCost(grid, costs, i, j, i+1, j)
    if j != len(grid[0])-1 and not visited[i][j+1]:
        updateCost(grid, costs, i, j, i, j+1)
    if i != 0 and not visited[i-1][j]:
        updateCost(grid, costs, i, j, i-1, j)
    if j != 0 and not visited[i][j-1]:
        updateCost(grid, costs, i, j, i, j-1)
