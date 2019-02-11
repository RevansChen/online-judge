# Python - 3.6.0

def sel_reverse(arr, l):
    if l == 0:
        return arr

    result = []
    left, right = 0, 0
    while right < len(arr):
        right = min(right + l, len(arr))
        result += sorted(arr[left:right], reverse = True)
        left = right

    return result
