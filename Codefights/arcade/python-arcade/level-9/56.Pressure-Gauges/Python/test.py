# Python3

from solution1 import pressureGauges as f

qa = [
    ([3, 5, 2, 6],
     [1, 6, 6, 6],
     [[1, 5, 2, 6],
      [3, 6, 6, 6]]),
    ([0, 12, 478, 23, 1000],
     [48, 23, 56, 23, 88],
     [[0, 12, 56, 23, 88],
      [48, 23, 478, 23, 1000]]),
    ([8],
     [1],
     [[1],
      [8]]),
    ([129, 553, 585],
     [852, 601, 997],
     [[129, 553, 585],
      [852, 601, 997]]),
    ([734, 483, 87, 499, 931, 657, 833],
     [316, 511, 592, 355, 819, 621, 419],
     [[316, 483, 87, 355, 819, 621, 419],
      [734, 511, 592, 499, 931, 657, 833]])
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
