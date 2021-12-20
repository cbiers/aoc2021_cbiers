import copy

def addOuter(im):
    res = []
    res.append(["-" for i in range(len(im[0]) + 2)])
    for line in im:
        new = []
        new.append("-")
        for c in line:
            new.append(c)
        new.append("-")
        res.append(new)
    res.append(["-" for i in range(len(im[0]) + 2)])
    return res

def countLit(im):
    count = 0
    for line in im:
        for el in line:
            if el == "#":
                count += 1
    return count

def toBit(c, t):
    if c == "#":
        return "1"
    elif c == "-":
        if t % 2 == 0:
            return "0"
        else:
            return "1"
    return "0"

def binToDec(b):
    res = 0
    for c in b:
        res *= 2
        res += int(c)
    return res

def enhance(im, al, turn):
    new = copy.deepcopy(im)
    for i in range(1, len(im)-1):
        for j in range(1, len(im[0])-1):
            byte = toBit(im[i-1][j-1], turn) + toBit(im[i-1][j], turn) + toBit(im[i-1][j+1], turn) + toBit(im[i][j-1], turn) + toBit(im[i][j], turn) + toBit(im[i][j+1], turn) + toBit(im[i+1][j-1], turn) + toBit(im[i+1][j], turn) + toBit(im[i+1][j+1], turn)
            new[i][j] = algorithm[binToDec(byte)]
    return new

f = open("in.txt", "r")
lines = f.readlines()

algorithm = lines[0][:-1]

image = []
for line in lines[2:]:
    image.append(line[:-1])
image = addOuter(addOuter(image))

for i in range(50):
    image = enhance(image, algorithm, i)
    image = addOuter(image)

print countLit(image)
