# Python3

from solution1 import leastCommonDenominator as f

qa = [
    ([2, 3, 4, 5, 6], 60),
    ([34, 6, 3, 5, 3], 510),
    ([2], 2),
    ([49, 23, 15, 20, 2, 42, 21, 34], 1149540),
    ([8, 19, 3, 5, 10, 2, 2, 4], 2280)
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
