# Python - 3.6.0

def is_sator_square(tablet):
    n = len(tablet)
    for r in range(n):
        for c in range(n):
            if not (tablet[r][c] == tablet[-(r + 1)][-(c + 1)] == tablet[c][r] == tablet[-(c + 1)][-(r + 1)]):
                return False
    return True
