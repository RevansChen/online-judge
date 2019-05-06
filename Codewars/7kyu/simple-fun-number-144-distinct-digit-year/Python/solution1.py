# Python - 3.6.0

def distinct_digit_year(year):
    for y in range(year + 1, 9001):
        if len(set(str(y))) == 4:
            return y
    return None
