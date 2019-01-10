# Python - 3.6.0

def animals(heads, legs):
    no_sol = 'No solutions'
    if (heads > 1000) or (heads < 0) or (legs > 1000) or (legs < 0) or ((legs % 2) == 1):
        return no_sol

    chickens = 2 * heads - legs // 2
    cows = legs // 2 - heads

    if (chickens < 0) or (cows < 0):
        return no_sol
    else:
        return (chickens, cows)
