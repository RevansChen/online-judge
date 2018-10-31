# Python3

from solution1 import mathPractice as f

qa = [
    ([1, 2, 3, 4, 5, 6], 71),
    ([8, 9], 17),
    ([0, 8, 15], 120),
    ([3, 18, 5, 17, 7, 12, 3, 14], 2612),
    ([9, 19, 2, 2, 7, 3, 0, 0, 6, 11, 14, 18, 11, 7, 9, 6, 8, 4, 13, 11], 1778151)
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
