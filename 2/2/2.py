f = open("in.txt", "r")
lines = f.readlines()

y = 0;
x = 0;
aim = 0;

for line in lines:
    sep = line.find(" ")
    dir = line[:sep]
    val = int(line[sep+1:-1])
    if dir == "up":
        aim -= val
    elif dir == "down":
        aim += val
    else:
        x += val
        y += aim * val

res = x * y
print res
