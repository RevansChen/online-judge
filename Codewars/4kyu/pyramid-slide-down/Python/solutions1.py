# Python - 2.7.6

def longest_slide_down(pyramid):
    for i in range(1, len(pyramid)):
        x = pyramid[-i]
        for j in range(len(x) - 1):
            pyramid[-(i+1)][j] += max(x[j], x[j + 1])
    return pyramid[0][0]