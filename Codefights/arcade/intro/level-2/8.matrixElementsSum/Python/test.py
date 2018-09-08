# Python3

from solution1 import matrixElementsSum as f

qa = [
    ([[0,1,1,2],
      [0,5,0,0],
      [2,0,3,3]], 9),
    ([[1,1,1,0],
      [0,5,0,1],
      [2,1,3,10]], 9),
    ([[1,1,1],
      [2,2,2],
      [3,3,3]], 18),
    ([[0]], 0)
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
