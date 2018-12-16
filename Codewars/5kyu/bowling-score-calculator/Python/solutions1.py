# Python - 3.6.0

def bowling_score(rolls):
    scores = [0] * 10
    idx = 0
    while len(rolls) > 0:
        roll = rolls.pop(0)
        if roll == 10:
            scores[idx] = 10 + sum(rolls[:2])
        else:
            roll2 = rolls.pop(0)
            sc = roll + roll2
            if sc == 10:
                scores[idx] = 10 + rolls[0]
            else:
                scores[idx] = sc
        idx += 1
        if idx == 9:
            break
    scores[idx] = sum(rolls)

    return sum(scores)
