f = open("in.txt", "r")
lines = f.readlines()
data = []
for line in lines:
    data.append([int(x) for x in line[:-1]])

sum = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if i != 0 and data[i-1][j] <= data[i][j]:
            continue
        if j != 0 and data[i][j-1] <= data[i][j]:
            continue
        if j != len(data[i])-1 and data[i][j+1] <= data[i][j]:
            continue
        if i != len(data)-1 and data[i+1][j] <= data[i][j]:
            continue
        sum += data[i][j] + 1

print sum
