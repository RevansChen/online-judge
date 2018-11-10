# Python - 3.4.3

def x(n):
    output = [ [ '□' ] * n for i in range(n) ]
    for i in range(n // 2 + 1):
        output[i][i] = output[i][-(i + 1)] = '■'
        output[n - i - 1][i] = output[n - i - 1][-(i + 1)] = '■'
    return '\n'.join(map(''.join, output))
