# Python - 3.6.0

def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != 1:
            return arr[i]
    return None
