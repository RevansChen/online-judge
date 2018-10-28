# Python3

from solution1 import rockPaperScissors as f

qa = [
    (['trainee', 'warrior', 'ninja'],
     [['ninja', 'trainee'],
      ['ninja', 'warrior'],
      ['trainee', 'ninja'],
      ['trainee', 'warrior'],
      ['warrior', 'ninja'],
      ['warrior', 'trainee']]),
    (['macho', 'hero'],
     [['hero', 'macho'],
      ['macho', 'hero']]),
    (['Professional player of great experience', 'Novice player with promising future', 'You', 'Player', 'I'],
     [['I', 'Novice player with promising future'],
      ['I', 'Player'],
      ['I', 'Professional player of great experience'],
      ['I', 'You'],
      ['Novice player with promising future', 'I'],
      ['Novice player with promising future', 'Player'],
      ['Novice player with promising future', 'Professional player of great experience'],
      ['Novice player with promising future', 'You'],
      ['Player', 'I'],
      ['Player', 'Novice player with promising future'],
      ['Player', 'Professional player of great experience'],
      ['Player', 'You'],
      ['Professional player of great experience', 'I'],
      ['Professional player of great experience', 'Novice player with promising future'],
      ['Professional player of great experience', 'Player'],
      ['Professional player of great experience', 'You'],
      ['You', 'I'],
      ['You', 'Novice player with promising future'],
      ['You', 'Player'],
      ['You', 'Professional player of great experience']]),
    (['Harry', 'Ron', 'Hermione', 'Draco', 'Tom'],
     [['Draco', 'Harry'],
      ['Draco', 'Hermione'],
      ['Draco', 'Ron'],
      ['Draco', 'Tom'],
      ['Harry', 'Draco'],
      ['Harry', 'Hermione'],
      ['Harry', 'Ron'],
      ['Harry', 'Tom'],
      ['Hermione', 'Draco'],
      ['Hermione', 'Harry'],
      ['Hermione', 'Ron'],
      ['Hermione', 'Tom'],
      ['Ron', 'Draco'],
      ['Ron', 'Harry'],
      ['Ron', 'Hermione'],
      ['Ron', 'Tom'],
      ['Tom', 'Draco'],
      ['Tom', 'Harry'],
      ['Tom', 'Hermione'],
      ['Tom', 'Ron']]),
    (['Luke', 'Leia', 'Padme', 'Anakin', 'Rey'],
     [['Anakin', 'Leia'],
      ['Anakin', 'Luke'],
      ['Anakin', 'Padme'],
      ['Anakin', 'Rey'],
      ['Leia', 'Anakin'],
      ['Leia', 'Luke'],
      ['Leia', 'Padme'],
      ['Leia', 'Rey'],
      ['Luke', 'Anakin'],
      ['Luke', 'Leia'],
      ['Luke', 'Padme'],
      ['Luke', 'Rey'],
      ['Padme', 'Anakin'],
      ['Padme', 'Leia'],
      ['Padme', 'Luke'],
      ['Padme', 'Rey'],
      ['Rey', 'Anakin'],
      ['Rey', 'Leia'],
      ['Rey', 'Luke'],
      ['Rey', 'Padme']]),
    (['A', 'B'],
     [['A', 'B'],
      ['B', 'A']])
]

for *q, a in qa:
    for i, e in enumerate(q):
        print('input{0}: {1}'.format(i + 1, e))
    ans = [*map(list, f(*q))]
    if ans != a:
        print('  [failed]')
        print('    output:', ans)
        print('    expected:', a)
    else:
        print('  [ok]')
        print('    output:', ans)
    print()
