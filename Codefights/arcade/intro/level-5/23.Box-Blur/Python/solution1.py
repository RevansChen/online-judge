# Python3

def boxBlur(image):
    results = []
    for r in range(1, len(image) - 1):
        line = []
        for c in range(1, len(image[r]) - 1):
            line.append(sum([sum(image[r - 1][c - 1:c + 2]), sum(image[r][c - 1:c + 2]), sum(image[r + 1][c - 1:c + 2])]) // 9)
        results.append(line)
    return results
