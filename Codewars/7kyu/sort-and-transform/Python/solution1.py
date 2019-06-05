# Python - 3.6.0

sort_transform = lambda arr: (lambda conv = lambda ls: ''.join(map(chr, ls[:2] + ls[-2:])): '-'.join([conv(arr), conv(sorted(arr)), conv(sorted(arr, reverse = True)), conv(sorted(arr))]))()
