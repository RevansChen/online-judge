# Python3

from solution1 import checkParticipants as f

qa = [
    ([0, 1, 1, 5, 4, 8],
     [2]),
    ([0, 1, 2, 3, 4, 5],
     []),
    ([6],
     []),
    ([3, 3, 3, 3, 3, 3, 3, 3],
     [4, 5, 6, 7]),
    ([0, 0, 1, 5, 5, 4, 5, 4, 10, 8],
     [1, 2, 5, 6, 7, 9])
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
