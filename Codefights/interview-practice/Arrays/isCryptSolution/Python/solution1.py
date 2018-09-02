# Python3

def isCryptSolution(crypt, solution):
    solution = { ord(s[0]): ord(s[1]) for s in solution }
    decrypt = [ c.translate(solution) for c in crypt ]
    for d in decrypt:
        if len(d) > 1 and d[0] == '0':
            return False
    decrypt = [*map(int, decrypt)]
    return (decrypt[0] + decrypt[1]) == decrypt[2]
