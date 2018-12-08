# Python - 2.7.6

def pascal(p):
    results = []
    if p > 0:
        results.append([1])
    if p > 0:
        for r in range(1, p):
            cs = [1]
            cs.extend([results[r - 1][c - 1] + results[r - 1][c] for c in range(1, r)])
            cs.append(1)
            results.append(cs)
    return results
