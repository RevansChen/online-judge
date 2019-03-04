# Python - 3.6.0

check_exam = lambda arr1, arr2: max(sum((4 * (a == b) - (a != b != '')) for a, b in zip(arr1, arr2)), 0)
