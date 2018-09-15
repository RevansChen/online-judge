# Python3

def depositProfit(deposit, rate, threshold):
    year, rate = 0, (1 + rate / 100)
    while deposit < threshold:
        deposit *= rate
        year += 1
    return year
