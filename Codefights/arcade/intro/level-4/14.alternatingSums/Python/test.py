# Python3

from solution1 import alternatingSums as f

qa = [
    ([50, 60, 60, 45, 70], [180, 105]),
    ([100, 50], [100, 50]),
    ([80], [80, 0]),
    ([100, 50, 50, 100], [150, 150]),
    ([100, 51, 50, 100], [150, 151])
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
