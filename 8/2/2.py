'''
0 - 6 digits
1 - 2 digits (unique)
2 - 5 digits
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

sum = 0

for line in lines:
    digits = line.split("|")[0][:-1].split(" ")
    output = line.split("|")[1][1:-1].split(" ")
    digits.sort(key=len)
    decoded = 0
    decode = {"1": "tbd", "3": "tbd", "6": "tbd"}
    for dd in digits:
        if len(dd) == 2:
            decode["1"] = dd
        elif len(dd) == 5:
            three = True
            for d in decode["1"]:
                if d not in dd:
                    three = False
                    break
            if three:
                decode["3"] = dd
        elif len(dd) == 6:
            six = True
            if decode["1"][0] in dd and decode["1"][1] in dd:
                six = False
            if six:
                decode["6"] = dd
    for out in output:
        dig = -1
        if len(out) == 2:
            dig = 1
        elif len(out) == 3:
            dig = 7
        elif len(out) == 4:
            dig = 4
        elif len(out) == 5:
            three = True
            for d in decode["1"]:
                if d not in out:
                    three = False
                    break
            if three:
                dig = 3
            else:
                five = True
                for d in out:
                    if d not in decode["6"]:
                        five = False
                if five:
                    dig = 5
                else:
                    dig = 2
        elif len(out) == 6:
            six = False
            for d in decode["1"]:
                if d not in out:
                    six = True
                    break
            if six:
                dig = 6
            else:
                nine = True
                for d in decode["3"]:
                    if d not in out:
                        nine = False
                        break
                if nine:
                    dig = 9
                else:
                    dig = 0
        else:
            dig = 8
        decoded = decoded * 10 + dig
    sum += decoded

print sum
