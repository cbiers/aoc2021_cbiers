def flash(data, x, y, flashed):
    flashed[x][y] = True
    flashes = 1
    data[x][y] = 0
    if x != 0:
        if y != 0:
            if not flashed[x-1][y-1]:
                data[x-1][y-1] += 1
                if data[x-1][y-1] > 9:
                    flashes += flash(data, x-1, y-1, flashed)
        if not flashed[x-1][y]:
            data[x-1][y] += 1
            if data[x-1][y] > 9:
                flashes += flash(data, x-1, y, flashed)
        if y != len(data)-1:
            if not flashed[x-1][y+1]:
                data[x-1][y+1] += 1
                if data[x-1][y+1] > 9:
                    flashes += flash(data, x-1, y+1, flashed)
    if x != len(data)-1:
        if y != 0:
            if not flashed[x+1][y-1]:
                data[x+1][y-1] += 1
                if data[x+1][y-1] > 9:
                    flashes += flash(data, x+1, y-1, flashed)
        if not flashed[x+1][y]:
            data[x+1][y] += 1
            if data[x+1][y] > 9:
                flashes += flash(data, x+1, y, flashed)
        if y != len(data)-1:
            if not flashed[x+1][y+1]:
                data[x+1][y+1] += 1
                if data[x+1][y+1] > 9:
                    flashes += flash(data, x+1, y+1, flashed)
    if y != 0:
        if not flashed[x][y-1]:
            data[x][y-1] += 1
            if data[x][y-1] > 9:
                flashes += flash(data, x, y-1, flashed)
    if y != len(data)-1:
        if not flashed[x][y+1]:
            data[x][y+1] += 1
            if data[x][y+1] > 9:
                flashes += flash(data, x, y+1, flashed)
    return flashes

f = open("in.txt", "r")
lines = f.readlines()

data = []

for line in lines:
    data.append([int(x) for x in line[:-1]])

flashes = 0
turn = 0
done = False

while not done:
    turn += 1
    for j in range(len(data)):
        for k in range(len(data)):
            data[j][k] += 1
    flashed = [[False for i in range(len(data))] for j in range(len(data))]
    for j in range(len(data)):
        for k in range(len(data)):
            if data[j][k] > 9:
                flashes += flash(data, j, k, flashed)
    allFlashed = True
    for j in range(len(data)):
        for i in range(len(data)):
            if data[i][j] != 0:
                allFlashed = False
                break
    if allFlashed:
        done = True

print turn
