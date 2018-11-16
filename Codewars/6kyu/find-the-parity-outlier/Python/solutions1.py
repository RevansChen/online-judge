# Python - 2.7.6

def find_outlier(integers):
    first3 = [ (i & 1, i) for i in integers[:3] ]
    first3.sort(key=lambda x: x[0])

    total = sum(i for i, _ in first3)
    if total == 1:
        return first3[-1][1]
    elif total == 2:
        return first3[0][1]

    rem = 1 if total else 0
    for i in integers[3:]:
        if (i & 1) != rem:
            return i
