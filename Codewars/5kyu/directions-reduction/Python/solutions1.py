# Python - 3.6.0

dic = {
    'NORTH' : 1,
    'SOUTH' : -1,

    'EAST' : 2,
    'WEST' : -2
}

def dirReduc(arr):
    results = []
    for e in arr:
        if (not results) or (dic[e] + dic[results[-1]]):
            results.append(e)
        else:
            results.pop()
    return results
