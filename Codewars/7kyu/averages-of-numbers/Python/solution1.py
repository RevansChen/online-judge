# Python - 3.6.0

def averages(arr):
    if type(arr) != list:
        return []
    if len(arr) < 2:
        return []

    result = []
    c = arr[0]
    for i in arr[1:]:
        result.append((c + i) / 2.0)
        c = i
    return result
