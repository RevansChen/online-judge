# Python3

from solution1 import convertTabs as f

qa = [
    ('\treturn False', 4,
     '    return False'),
    ('', 8,
     ''),
    ('    for x in range(20)', 16,
     '    for x in range(20)'),
    ('def add(x, y)\f\treturn x + y', 8,
     'def add(x, y)\f        return x + y'),
    ('\t\t\t\t\t', 4,
     '                    '),
    ('\treturn\t', 2,
     '  return  '),
    ('\tyield\t', 7,
     '       yield       '),
    ("here's a test where nothing should be replaced", 3,
     "here's a test where nothing should be replaced")
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
