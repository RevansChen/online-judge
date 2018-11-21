# Python - 3.6.0

def high_and_low(numbers):
    lst = [*map(int, numbers.split(' '))]
    return f'{max(lst)} {min(lst)}'
