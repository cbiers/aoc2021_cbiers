f = open("in.txt", "r")
lines = f.readlines()

seq = lines[0].strip()
subs = {}

for line in lines[2:]:
    parts = line.split(" -> ")
    subs[parts[0]] = parts[1].strip()

for i in range(10):
    newseq = seq[0]
    for j in range(len(seq)-1):
        newseq += subs[seq[j:j+2]] + seq[j+1]
    seq = newseq

occurences = {}
for val in set(subs.values()):
    occurences[val] = 0

for c in seq:
    occurences[c] += 1

print max(occurences.values()) - min(occurences.values())
