# Python3

from solution1 import almostIncreasingSequence as f

qa = [
    ([1, 2, 3, 4, 5], True),
    ([1, 3, 2, 1], False),
    ([1, 3, 2], True),
    ([1, 2, 1, 2], False),
    ([1, 4, 10, 4, 2], False),
    ([10, 1, 2, 3, 4, 5], True),
    ([1, 1, 1, 2, 3], False),
    ([0, -2, 5, 6], True),
    ([1, 2, 3, 4, 5, 3, 5, 6], False),
    ([40, 50, 60, 10, 20, 30], False),
    ([1, 1], True),
    ([1, 2, 5, 3, 5], True),
    ([1, 2, 5, 5, 5], False),
    ([10, 1, 2, 3, 4, 5, 6, 1], False),
    ([1, 2, 3, 4, 3, 6], True),
    ([1, 2, 3, 4, 99, 5, 6], True),
    ([123, -17, -5, 1, 2, 3, 12, 43, 45], True),
    ([3, 5, 67, 98, 3], True)
]

for *q, a in qa:
    for i, e in enumerate(q):
        print('input{0}: {1}'.format(i + 1, e))
    ans = f(*q)
    if ans != a:
        print('  [failed]')
        print('    output:', ans)
        print('    expected:', a)
    else:
        print('  [ok]')
        print('    output:', ans)
    print()
