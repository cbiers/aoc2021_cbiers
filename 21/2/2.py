f = open("in.txt", "r")
lines = f.readlines()

scores = [{"score1": 0, "score2": 0, "occurences": 1, "pos1": int(lines[0][-2]), "pos2": int(lines[1][-2])}]
outcomes =  [
                {"roll": 3, "prob": 1},
                {"roll": 4, "prob": 3},
                {"roll": 5, "prob": 6},
                {"roll": 6, "prob": 7},
                {"roll": 7, "prob": 6},
                {"roll": 8, "prob": 3},
                {"roll": 9, "prob": 1}
            ]
wins = [0, 0]

currentPlayer = 1

while scores:
    print len(scores)
    newScores = []
    for s in scores:
        if s["score1"] < 21 and s["score2"] < 21:
            for o in outcomes:
                if currentPlayer == 1:
                    newPos = s["pos1"] + o["roll"]
                    if newPos > 10:
                        newPos -= 10
                    newScore = s["score1"] + newPos
                    newScore = {"score1": newScore, "score2": s["score2"], "occurences": o["prob"] * s["occurences"], "pos1": newPos, "pos2": s["pos2"]}
                else:
                    newPos = s["pos2"] + o["roll"]
                    if newPos > 10:
                        newPos -= 10
                    newScore = s["score2"] + newPos
                    newScore = {"score2": newScore, "score1": s["score1"], "occurences": o["prob"] * s["occurences"], "pos2": newPos, "pos1": s["pos1"]}
                newScores.append(newScore)
        else:
            if s["score1"] >= 21:
                wins[0] += s["occurences"]
            else:
                wins[1] += s["occurences"]
    if currentPlayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1
    scores = newScores

print wins
