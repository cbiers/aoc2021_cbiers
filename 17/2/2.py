f = open("in.txt", "r")
line = f.readlines()[0][:-1]

xMin = int(line[15:18])
xMax = int(line[20:23])
yMin = int(line[27:31])
yMax = int(line[33:36])

count = 0

for i in range(194):
    for j in range(-200, 200):
        x = 0
        y = 0
        xVel = i
        yVel = j
        while y >= yMin:
            x += xVel
            y += yVel
            if xVel > 0:
                xVel -= 1
            elif xVel < 0:
                xVel += 1
            yVel -= 1
            if x >= xMin and x <= xMax and y >= yMin and y <= yMax:
                count += 1
                break

print count
