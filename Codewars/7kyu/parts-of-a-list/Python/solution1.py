# Python - 3.6.0

partlist = lambda arr: [(' '.join(arr[:i + 1]), ' '.join(arr[i + 1:])) for i in range(len(arr) - 1)]
