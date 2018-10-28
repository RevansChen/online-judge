# Python3

from solution1 import kthPermutation as f

qa = [
    ([1, 2, 3, 4, 5], 4,
     [1, 2, 4, 5, 3]),
    ([1, 2], 1,
     [1, 2]),
    ([11, 22, 31, 43, 56], 120,
     [56, 43, 31, 22, 11]),
    ([14, 25, 27, 29, 30, 40, 55, 89, 100, 239], 238,
     [14, 25, 27, 29, 40, 239, 100, 55, 89, 30]),
    ([14, 25, 27, 29, 30, 40, 55, 89, 100, 239], 3628800,
     [239, 100, 89, 55, 40, 30, 29, 27, 25, 14]),
    ([50, 100, 123, 789], 15,
     [123, 100, 50, 789])
]

for *q, a in qa:
    for i, e in enumerate(q):
        print('input{0}: {1}'.format(i + 1, e))
    ans = list(f(*q))
    if ans != a:
        print('  [failed]')
        print('    output:', ans)
        print('    expected:', a)
    else:
        print('  [ok]')
        print('    output:', ans)
    print()
