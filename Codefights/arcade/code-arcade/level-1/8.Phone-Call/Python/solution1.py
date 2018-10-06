# Python3

def phoneCall(min1, min2_10, min11, s):
    funcs = [
        lambda cost, money: (1, money - cost, False) if money >= cost else (0, money, True),
        lambda cost, money: (min(9, money // cost), money - min(9, money // cost) * cost, (money - min(9, money // cost) * cost) < cost),
        lambda cost, money: (money // cost, money - (money // cost) * cost, False)
    ]
    duration = 0
    costs = [min1, min2_10, min11]
    for i, func in enumerate(funcs):
        dur, s, end = func(costs[i], s)
        duration += dur
        if end:
            break

    return duration
