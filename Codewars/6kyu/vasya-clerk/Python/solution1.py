# Python - 3.6.0

def tickets(people):
    moneys = {k: 0 for k in [25, 50, 100]}
    for cost in people:
        if cost == 50:
            if moneys[25] < 1:
                return 'NO'
            moneys[25] -= 1
        elif cost == 100:
            if moneys[50] >= 1:
                if moneys[25] < 1:
                    return 'NO'
                moneys[50] -= 1
                moneys[25] -= 1
            else:
                if moneys[25] < 3:
                    return 'NO'
                moneys[25] -= 3
        moneys[cost] += 1
    return 'YES'

