# Python - 3.6.0

import re

def arrange(arr):
    units = {
        'G': 1,
        'KG': 1000,
        'T': 1000000
    }
    newArr = []
    for i in range(len(arr)):
        w = arr[i]
        sp = re.match('^\d+', w).span()[1]
        val, unit = int(w[:sp]), w[sp:]
        val *= units[unit]
        newArr.append((val, w))
    newArr.sort(key=lambda x: x[0])
    return [ e[1] for e in newArr ]
