f = open("in.txt", "r")
line = f.readlines()[0][:-1]

xMin = int(line[15:18])
xMax = int(line[20:23])
yMin = int(line[27:31])
yMax = int(line[33:36])

best = -100000

for i in range(194):
    for j in range(200):
        x = 0
        y = 0
        xVel = i
        yVel = j
        hit = False
        maxY = -100000
        while y >= yMin:
            x += xVel
            y += yVel
            if y > maxY:
                maxY = y
            if xVel > 0:
                xVel -= 1
            elif xVel < 0:
                xVel += 1
            yVel -= 1
            if x >= xMin and x <= xMax and y >= yMin and y <= yMax:
                hit = True
                break
        if hit and maxY > best:
                best = maxY

print best
