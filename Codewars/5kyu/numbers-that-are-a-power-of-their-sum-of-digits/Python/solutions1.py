# Python - 3.6.0

def sumDigits(val):
    result = 0
    while val > 0:
        val, rem = divmod(val, 10)
        result += rem
    return result

def addTerms(terms, length):
    from math import log

    minVal, maxVal = (10 ** (length - 1), (10 ** length) - 1)
    newTerms = []
    for s in range(2, 9 * length):
        val = s ** (int(log(minVal, s)) + 1)

        while val <= maxVal:
            if s == sumDigits(val):
                newTerms.append(val)
                break
            val *= s

    terms.extend(sorted(newTerms))

def power_sumDigTerm(n):
    terms = []
    length = 2
    while n > len(terms):
        addTerms(terms, length)
        length += 1
    return terms[n - 1]
