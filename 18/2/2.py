import json
import math
import copy

def add(n, t):
    return [n, t]

def maxDepth(n):
    max = 1
    for el in n:
        if isinstance(el, list):
            depth = 1 + maxDepth(el)
            if depth > max:
                max = depth
    return max

def mustExplode(n):
    return maxDepth(n) >= 5

def mustSplit(n):
    split = False
    for el in n:
        if not isinstance(el, list) and el >= 10:
            split = True
        elif isinstance(el, list):
            if mustSplit(el):
                split = True
    return split

def addLeft(n, i, d):
    if isinstance(n[i], list):
        addLeft(n[i], len(n)-1, d)
    else:
        n[i] += d

def addRight(n, i, d):
        if isinstance(n[i], list):
            addRight(n[i], 0, d)
        else:
            n[i] += d

def explodeRec(n, d):
    if d == 4:
        for i in range(len(n)):
            if isinstance(n[i], list):
                addToLeft = False
                addToRight = False
                if i != 0:
                    addLeft(n, i-1, n[i][0])
                else:
                    addToLeft = n[i][0]
                if i != len(n)-1:
                    addRight(n, i+1, n[i][1])
                else:
                    addToRight = n[i][1]
                n[i] = 0
                return [addToLeft, addToRight, True]
    else:
        for i in range(len(n)):
            if isinstance(n[i], list):
                e = explodeRec(n[i], d+1)
                if e[2]:
                    addToLeft = False
                    addToRight = False
                    if e[0]:
                        if i != 0:
                            addLeft(n, i-1, e[0])
                        else:
                            addToLeft = e[0]
                    if e[1]:
                        if i != len(n)-1:
                            addRight(n, i+1, e[1])
                        else:
                            addToRight = e[1]
                    return [addToLeft, addToRight, True]
    return [False, False, False]

def explode(n):
    explodeRec(n, 1)

def split(n):
    for i in range(len(n)):
        if not isinstance(n[i], list) and n[i] >= 10:
            n[i] = [(n[i] / 2), int(math.ceil(float(n[i]) / 2))]
            return True
        elif isinstance(n[i], list):
            s = split(n[i])
            if s:
                return True
    return False

def reduce(n):
    e = mustExplode(n)
    s = mustSplit(n)
    while e or s:
        if e:
            explode(n)
            e = mustExplode(n)
            s = mustSplit(n)
            continue
        if s:
            split(n)
            e = mustExplode(n)
            s = mustSplit(n)
            continue
    return n

def magnitude(n):
    if not isinstance(n, list):
        return n
    else:
        return 3 * magnitude(n[0]) + 2 * magnitude(n[1])

f = open("in.txt", "r")
lines = f.readlines()

nums = [json.loads(lines[i]) for i in range(len(lines))]

best = 0

for num in nums:
    for num2 in nums:
        if num != num2:
            curr = magnitude(reduce(add(copy.deepcopy(num), copy.deepcopy(num2))))
            if curr > best:
                best = curr
            curr = magnitude(reduce(add(copy.deepcopy(num2), copy.deepcopy(num))))
            if curr > best:
                best = curr

print best
