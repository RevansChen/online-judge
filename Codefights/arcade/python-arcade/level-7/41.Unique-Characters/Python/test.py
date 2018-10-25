# Python3

from solution1 import uniqueCharacters as f

qa = [
    ('Todd told Tom to trot to the timber',
     [' ', 'T', 'b', 'd', 'e', 'h', 'i', 'l', 'm', 'o', 'r', 't']),
    ('Brilliant, because bacon bites beat bruschetta',
     [' ', ',', 'B', 'a', 'b', 'c', 'e', 'h', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']),
    ('Veni, Vidi, Vici',
     [' ', ',', 'V', 'c', 'd', 'e', 'i', 'n']),
    ('codefighter fight codefighter with code',
     [' ', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'o', 'r', 't', 'w']),
    ('I',
     ['I'])
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
