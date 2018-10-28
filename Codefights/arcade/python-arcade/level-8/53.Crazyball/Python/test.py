# Python3

from solution1 import crazyball as f

qa = [
    (['Ninja',
      'Warrior',
      'Trainee',
      'Newbie'], 3,
     [['Newbie', 'Ninja', 'Trainee'],
      ['Newbie', 'Ninja', 'Warrior'],
      ['Newbie', 'Trainee', 'Warrior'],
      ['Ninja', 'Trainee', 'Warrior']]),
    (['Ninja',
      'Warrior',
      'Trainee',
      'Newbie'], 4,
     [['Newbie', 'Ninja', 'Trainee', 'Warrior']]),
    (['Pooh'], 1,
     [['Pooh']]),
    (['Browny',
      'Whitey',
      'Blacky'], 1,
     [['Blacky'],
      ['Browny'],
      ['Whitey']]),
    (['One',
      'Two',
      'Three',
      'Four',
      'Five',
      'Six',
      'Seven'], 5,
     [['Five', 'Four', 'One', 'Seven', 'Six'],
      ['Five', 'Four', 'One', 'Seven', 'Three'],
      ['Five', 'Four', 'One', 'Seven', 'Two'],
      ['Five', 'Four', 'One', 'Six', 'Three'],
      ['Five', 'Four', 'One', 'Six', 'Two'],
      ['Five', 'Four', 'One', 'Three', 'Two'],
      ['Five', 'Four', 'Seven', 'Six', 'Three'],
      ['Five', 'Four', 'Seven', 'Six', 'Two'],
      ['Five', 'Four', 'Seven', 'Three', 'Two'],
      ['Five', 'Four', 'Six', 'Three', 'Two'],
      ['Five', 'One', 'Seven', 'Six', 'Three'],
      ['Five', 'One', 'Seven', 'Six', 'Two'],
      ['Five', 'One', 'Seven', 'Three', 'Two'],
      ['Five', 'One', 'Six', 'Three', 'Two'],
      ['Five', 'Seven', 'Six', 'Three', 'Two'],
      ['Four', 'One', 'Seven', 'Six', 'Three'],
      ['Four', 'One', 'Seven', 'Six', 'Two'],
      ['Four', 'One', 'Seven', 'Three', 'Two'],
      ['Four', 'One', 'Six', 'Three', 'Two'],
      ['Four', 'Seven', 'Six', 'Three', 'Two'],
      ['One', 'Seven', 'Six', 'Three', 'Two']])
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
