# Python3

from solution1 import memoryPills as f

qa = [
    (['Notforgetan', 'Antimoron', 'Rememberin', 'Bestmedicen', 'Superpillsus'],
     ['Bestmedicen', 'Superpillsus', '']),
    (['Pillin'],
     ['', '', '']),
    (['Med 1', 'Med 2', 'Med 3', 'Med 10', 'Med 11', 'Med 12', 'Med 14', 'Med 42', 'Med 239'],
     ['Med 11', 'Med 12', 'Med 14']),
    (['Pills', 'Shmills', 'Medicine', 'Phedicine', 'Hey', 'Hoy'],
     ['Phedicine', 'Hey', 'Hoy']),
    (['Test', 'Where', 'The', 'First', 'Element', 'Is', 'Even'],
     ['Where', 'The', 'First'])
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
