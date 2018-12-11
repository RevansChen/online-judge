# Python - 2.7.6

def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal *= (1 + interest * (1 - tax))
        years += 1
    return years
