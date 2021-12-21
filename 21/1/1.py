def getNextThreeRolls(n):
    return [n % 100, (n+1) % 100, (n+2) % 100]

f = open("in.txt", "r")
lines = f.readlines()

positions = [int(lines[0][-2])-1, int(lines[1][-2])-1]
scores = [0, 0]

currentDie = 0
currentPlayer = 0

rollCount = 0

while scores[0] < 1000 and scores[1] < 1000:
    rolls = getNextThreeRolls(currentDie)
    for i in rolls:
        positions[currentPlayer] = (positions[currentPlayer] + (i+1)) % 10
    scores[currentPlayer] += positions[currentPlayer] + 1
    currentDie = rolls[2] + 1
    rollCount += 3
    if currentPlayer == 0:
        currentPlayer = 1
    else:
        currentPlayer = 0

print rollCount * min(scores)
