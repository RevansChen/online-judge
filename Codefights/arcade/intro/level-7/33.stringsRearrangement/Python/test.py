# Python3

from solution1 import stringsRearrangement as f

qa = [
    (['aba', 'bbb', 'bab'], False),
    (['ab', 'bb', 'aa'], True),
    (['q', 'q'], False),
    (['zzzzab', 'zzzzbb', 'zzzzaa'], True),
    (['ab', 'ad', 'ef', 'eg'], False),
    (['abc', 'bef', 'bcc', 'bec', 'bbc', 'bdc'], True),
    (['abc', 'abx', 'axx', 'abc'], False),
    (['abc', 'abx', 'axx', 'abx', 'abc'], True),
    (['f', 'g', 'a', 'h'], True),
    (['ff', 'gf', 'af', 'ar', 'hf'], True),
    (['a', 'b', 'c'], True)
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
