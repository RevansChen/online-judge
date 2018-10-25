# Python3

from solution1 import startupName as f

qa = [
    (['coolcompany', 'nicecompany', 'legendarycompany'],
     ['e', 'l']),
    (['nameone', 'nametwo', 'namethree'],
     ['o', 't']),
    (['heh', 'hah', 'funny'],
     ['h']),
    (['amazon', 'ebay', 'aliexpress'],
     ['e']),
    (['abc', 'def', 'hijk'],
     []),
    (['cool', 'looc', 'loco'],
     [])
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
