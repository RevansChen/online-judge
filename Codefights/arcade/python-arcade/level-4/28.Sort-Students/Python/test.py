# Python3

from solution1 import sortStudents as f

qa = [
    (['John Smith',
      'Jacky Mon Simonoff',
      'Lucy Smith',
      'Angela Zimonova'],
     ['Jacky Mon Simonoff',
      'John Smith',
      'Lucy Smith',
      'Angela Zimonova']),
    (['Lucy Smith',
      'John Smith',
      'Jacky Mon Simonoff',
      'Angela Zimonova'],
     ['Jacky Mon Simonoff',
      'Lucy Smith',
      'John Smith',
      'Angela Zimonova']),
    (['Kate'],
     ['Kate']),
    (['Massuginn Dragonbrewer',
      'Gragrinelynn Chainbasher',
      'Barirud Treasureforged',
      'Orimir Rubyheart',
      'Krathoun Flatbuster',
      'Museagret Browngrog',
      'Groodgratelin Magmabuckle'],
     ['Museagret Browngrog',
      'Gragrinelynn Chainbasher',
      'Massuginn Dragonbrewer',
      'Krathoun Flatbuster',
      'Groodgratelin Magmabuckle',
      'Orimir Rubyheart',
      'Barirud Treasureforged']),
    (['Massuginn Dragonbrewer',
      'Nomneare Windback',
      'Nurgutrude Strongpike',
      'Barirud Treasureforged',
      'Rudrud Lavahelm',
      'Asseam Coindelver',
      'Krathoun Flatbuster',
      'Museagret Browngrog',
      'Gorbaebelle Brickbelt',
      'Groodgratelin Magmabuckle'],
     ['Gorbaebelle Brickbelt',
      'Museagret Browngrog',
      'Asseam Coindelver',
      'Massuginn Dragonbrewer',
      'Krathoun Flatbuster',
      'Rudrud Lavahelm',
      'Groodgratelin Magmabuckle',
      'Nurgutrude Strongpike',
      'Barirud Treasureforged',
      'Nomneare Windback']),
    (['John Doe',
      'Brick Tick',
      'Batman'],
     ['Batman',
      'John Doe',
      'Brick Tick'])
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
