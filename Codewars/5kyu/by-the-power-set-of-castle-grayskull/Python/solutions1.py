# Python - 2.7.6

def power(s):
    sublists, bits = [], [0] * len(s)
    while bits[-1] != 2:
        sublists.append([e for i, e in enumerate(s) if bits[i]])

        bits[0] += 1
        for i in range(len(s) - 1):
            if bits[i] == 2:
                bits[i + 1] += 1
                bits[i] = 0
    return sublists
