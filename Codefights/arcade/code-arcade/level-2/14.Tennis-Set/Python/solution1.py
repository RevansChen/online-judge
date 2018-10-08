# Python3

def tennisSet(score1, score2):
    a, b = max(score1, score2), min(score1, score2)
    return (a == 6 and b < 5) or (a == 7 and b in [5, 6])
