# Python3

def countSumOfTwoRepresentations2(n, l, r):
    A = n // 2
    B = n - A
    return min(A - l, r - B) + 1 if l <= A <= B <= r else 0
