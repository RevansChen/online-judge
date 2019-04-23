# Python - 3.6.0

def nb_year(p0, percent, aug, p):
    percent = percent * 0.01 if percent else 0
    curr, year = p0, 0
    while curr < p:
        year += 1
        curr = int(curr * (1 + percent) + aug)
    return year

