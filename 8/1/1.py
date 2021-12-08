'''
0 - 6 digits
1 - 2 digits (unique)
3 - 5 digits
4 - 4 digits (unique)
5 - 5 digits
6 - 6 digits
7 - 3 digits (unique)
8 - 7 digits (unique)
9 - 6 digits
'''

f = open("in.txt", "r")
lines = f.readlines()

count = 0

for line in lines:
    digits = line.split("|")[0][:-1].split(" ")
    output = line.split("|")[1][1:-1].split(" ")
    for out in output:
        if len(out) in (2, 4, 3, 7):
            count += 1

print count
