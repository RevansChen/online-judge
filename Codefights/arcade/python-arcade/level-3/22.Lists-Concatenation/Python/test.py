# Python3

from solution1 import listsConcatenation as f

qa = [
    ([2, 2, 1],
     [10, 11],
     [2, 2, 1, 10, 11]),
    ([2, 4, 2, 34, 5],
     [],
     [2, 4, 2, 34, 5]),
    ([],
     [5, 3, -2, 0],
     [5, 3, -2, 0]),
    ([2, 4, 56, 7, 34, 2, 4, 6, 0],
     [6, 3, 5, 23, 2, 4, 6, 67, 9],
     [2, 4, 56, 7, 34, 2, 4, 6, 0, 6, 3, 5, 23, 2, 4, 6, 67, 9]),
    ([2, 6, 3, 5],
     [1],
     [2, 6, 3, 5, 1])
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
