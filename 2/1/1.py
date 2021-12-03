f = open("in.txt", "r")
lines = f.readlines()

y = 0;
x = 0;

for line in lines:
    sep = line.find(" ")
    dir = line[:sep]
    val = int(line[sep+1:-1])
    if dir == "up":
        y -= val
    elif dir == "down":
        y += val
    else:
        x += val

res = x * y
print res
