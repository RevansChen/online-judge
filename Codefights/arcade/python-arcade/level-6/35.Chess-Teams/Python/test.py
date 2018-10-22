# Python3

from solution1 import chessTeams as f

qa = [
    (['Jane', 'Bob', 'Peter'],
     ['Oscar', 'Lidia', 'Ann'],
     [['Jane', 'Oscar'],
      ['Bob', 'Lidia'],
      ['Peter', 'Ann']]),
    ([],
     [],
     []),
    (['Harry', 'Hermione', 'Ron', 'Albus'],
     ['Draco', 'Crabbe', 'Goyle', 'Tom'],
     [['Harry', 'Draco'],
      ['Hermione', 'Crabbe'],
      ['Ron', 'Goyle'],
      ['Albus', 'Tom']]),
    (['Luke', 'Leia'],
     ['Anakin', 'Padme'],
     [['Luke', 'Anakin'],
      ['Leia', 'Padme']]),
    (['Gandalf'],
     ['Saruman'],
     [['Gandalf', 'Saruman']])
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
