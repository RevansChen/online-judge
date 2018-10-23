# Python3

from solution1 import fixResult as f

qa = [
    ([42, 239, 365, 50],
     [4, 23, 36, 5]),
    ([],
     []),
    ([31, 41, 59, 26, 53, 58, 97, 93],
     [3, 4, 5, 2, 5, 5, 9, 9]),
    ([100000],
     [10000]),
    ([23, 73467, 1737, 4837, 2748, 27847, 2847, 249, 9367],
     [2, 7346, 173, 483, 274, 2784, 284, 24, 936])
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
