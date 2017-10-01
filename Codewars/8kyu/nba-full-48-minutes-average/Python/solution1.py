# Python - 2.7.6

def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    return round((48.0 / mpg) * ppg, 1)