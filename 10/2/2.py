f = open("in.txt", "r")
lines = f.readlines()

closing = {")": 3, "]": 57, "}": 1197, ">": 25137}

scores = []

for line in lines:
    stack = []
    corrupted = False
    for c in line[:-1]:
        if c not in closing.keys():
            stack.append(c)
        else:
            o = stack.pop()
            if not(c == ")" and o == "(" or c == "]" and o == "[" or c == ">" and o == "<" or c == "}" and o == "{"):
                corrupted = True
                break
    if not corrupted:
        val = 0
        while len(stack) > 0:
            val *= 5
            el = stack.pop()
            if el == "(":
                val += 1
            elif el == "[":
                val += 2
            elif el == "{":
                val += 3
            else:
                val += 4
        scores.append(val)

scores.sort()
print scores[len(scores)/2]
