# Python3

from solution1 import twinsScore as f

qa = [
    ([22, 13, 45, 32],
     [28, 41, 13, 32],
     [50, 54, 58, 64]),
    ([0, 0, 0],
     [100, 100, 100],
     [100, 100, 100]),
    ([42],
     [42],
     [84]),
    ([46, 22, 2, 83, 15, 46, 98],
     [28, 33, 91, 71, 77, 35, 5],
     [74, 55, 93, 154, 92, 81, 103]),
    ([73, 5, 69, 88, 53, 8, 25, 52, 18, 61],
     [97, 61, 69, 10, 11, 13, 72, 3, 57, 47],
     [170, 66, 138, 98, 64, 21, 97, 55, 75, 108])
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
