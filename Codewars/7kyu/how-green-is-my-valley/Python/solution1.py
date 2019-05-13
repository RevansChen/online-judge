# Python - 3.6.0

make_valley = lambda arr: (lambda a = sorted(arr, reverse = True): a[::2] + a[1::2][::-1])()
