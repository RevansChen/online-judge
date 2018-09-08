# Python3

from solution1 import areSimilar as f

qa = [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2, 3], [2, 1, 3], True),
    ([1, 2, 2], [2, 1, 1], False),
    ([1, 1, 4], [1, 2, 3], False),
    ([1, 2, 3], [1, 10, 2], False),
    ([2, 3, 1], [1, 3, 2], True),
    ([2, 3, 9], [10, 3, 2], False),
    ([4, 6, 3], [3, 4, 6], False),
    ([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 998, 148, 570, 533, 561, 455, 147, 894, 279], True),
    ([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279], False)
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
