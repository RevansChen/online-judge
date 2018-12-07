# Python - 3.6.0

def get_length_of_missing_array(array_of_arrays):
    isNoneOrEmpty = lambda arr: not arr

    if isNoneOrEmpty(array_of_arrays):
        return 0

    lengths = []
    for arr in array_of_arrays:
        if isNoneOrEmpty(arr):
            return 0
        lengths.append(len(arr))
    lengths.sort()

    for i in range(lengths[0], lengths[-1]):
        if not (i in lengths):
            return i
    return 0
