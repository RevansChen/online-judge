# Python - 3.6.0

def easyline(n):
    fac = {0: 1}
    for i in range(1, 2 * n + 1):
        fac[i] = fac[i - 1] * i
    return fac[n * 2] // (fac[n] * fac[n])
