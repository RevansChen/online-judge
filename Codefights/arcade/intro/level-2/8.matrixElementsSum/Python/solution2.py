# Python3

def matrixElementsSum(matrix):
    total = 0
    for c in range(len(matrix[0])):
        for r in range(len(matrix)):
            if matrix[r][c] == 0:
                break
            total += matrix[r][c]
    
    return total
