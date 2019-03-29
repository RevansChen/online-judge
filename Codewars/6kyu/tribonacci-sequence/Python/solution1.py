# Python - 3.6.0

def tribonacci(signature, n):
    array = signature.copy()
    for i in range(n - 3):
        array.append(array[-1] + array[-2] + array[-3])
    return array[:n]
