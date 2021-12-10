f = open("in.txt", "r")
lines = f.readlines()

closing = {")": 3, "]": 57, "}": 1197, ">": 25137}
counters = {")": 0, "]": 0, "}": 0, ">": 0}

for line in lines:
    stack = []
    for c in line[:-1]:
        if c not in closing.keys():
            stack.append(c)
        else:
            o = stack.pop()
            if not(c == ")" and o == "(" or c == "]" and o == "[" or c == ">" and o == "<" or c == "}" and o == "{"):
                counters[c] += 1
                break

sum = 0
for key in closing.keys():
    sum += closing[key] * counters[key]

print sum
