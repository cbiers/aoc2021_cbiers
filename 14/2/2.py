f = open("in.txt", "r")
lines = f.readlines()

seq = lines[0].strip()
subs = {}

for line in lines[2:]:
    parts = line.split(" -> ")
    subs[parts[0]] = parts[1].strip()

pairs = {}
for pair in subs.keys():
    pairs[pair] = 0

for i in range(len(seq)-1):
    pairs[seq[i:i+2]] += 1

for i in range(40):
    pairs2 = pairs.copy()
    for pair in pairs.keys():
        if pairs[pair] != 0:
            pairs2[pair[0] + subs[pair]] += pairs[pair]
            pairs2[subs[pair] + pair[1]] += pairs[pair]
            pairs2[pair] -= pairs[pair]
    pairs = pairs2

occurences = {}
for val in set(subs.values()):
    occurences[val] = 0

for pair in pairs.keys():
    occurences[pair[0]] += pairs[pair]
    occurences[pair[1]] += pairs[pair]

for occ in occurences.keys():
    occurences[occ] /= 2

occurences[seq[0]] += 1
occurences[seq[-1]] += 1

print max(occurences.values()) - min(occurences.values())
