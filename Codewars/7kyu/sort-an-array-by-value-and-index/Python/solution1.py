# Python - 3.6.0

def sort_by_value_and_index(arr):
    prodv = [(arr[i], arr[i] * (i + 1)) for i in range(len(arr))]
    return [e[0] for e in sorted(prodv, key = lambda x: x[1])]
