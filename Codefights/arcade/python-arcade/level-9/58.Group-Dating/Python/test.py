# Python3

from solution1 import groupDating as f

qa = [
    ([5, 28, 14, 99, 17],
     [5, 14, 28, 99, 16],
     [[28, 14, 17],
      [14, 28, 16]]),
    ([42],
     [64],
     [[42],
      [64]]),
    ([1, 2, 3, 4],
     [1, 2, 3, 4],
     [[],
      []]),
    ([6, 23, 82],
     [82, 56, 92],
     [[6, 23, 82],
      [82, 56, 92]]),
    ([0, 34, 100, 81, 100, 82, 0],
     [46, 34, 100, 76, 20, 82, 44],
     [[0, 81, 100, 0],
      [46, 76, 20, 44]])
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
