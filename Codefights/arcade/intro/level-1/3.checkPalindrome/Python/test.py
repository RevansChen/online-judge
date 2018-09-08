# Python3

from solution1 import checkPalindrome as f

qa = [
    ("aabaa", True),
    ("abac", False),
    ("a", True),
    ("az", False),
    ("abacaba", True),
    ("z", True),
    ("aaabaaaa", False),
    ("zzzazzazz", False),
    ("hlbeeykoqqqqokyeeblh", True),
    ("hlbeeykoqqqokyeeblh", True)
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
