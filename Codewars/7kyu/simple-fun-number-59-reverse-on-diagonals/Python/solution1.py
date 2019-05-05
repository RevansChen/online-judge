# Python - 3.6.0

def reverse_on_diagonals(matrix):
    for i in range(len(matrix) // 2):
        j = -(i + 1)
        matrix[i][i], matrix[j][j], matrix[j][i], matrix[i][j] = matrix[j][j], matrix[i][i], matrix[i][j], matrix[j][i]
    return matrix
