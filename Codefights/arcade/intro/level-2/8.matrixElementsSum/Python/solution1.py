def matrixElementsSum(matrix):
    for c in range(len(matrix[0])):
        for r in range(len(matrix)):
            if matrix[r][c] == 0:
                for ir in range(r + 1, len(matrix)):
                    matrix[ir][c] = 0
                break

    return sum(sum(r) for r in matrix)
