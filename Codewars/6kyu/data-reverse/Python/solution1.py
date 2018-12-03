# Python - 3.6.0

def data_reverse(data):
    b = 8
    num = len(data) // b
    rev = []
    for i in range((num - 1) * b, -1, -b):
        rev += data[i:i + b]
    return rev
