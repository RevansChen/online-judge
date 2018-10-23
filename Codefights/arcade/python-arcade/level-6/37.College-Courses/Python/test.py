# Python3

from solution1 import collegeCourses as f

qa = [
    (7, ['Art', 'Finance', 'Business', 'Speech', 'History', 'Writing', 'Statistics'],
     ['Art', 'Business', 'Speech', 'Statistics']),
    (5, ['Botany', 'Earth', 'Public Water Works', 'Biology', 'Zoology', 'Combat'],
     ['Botany', 'Public Water Works', 'Biology', 'Zoology', 'Combat']),
    (10, ['Negotiations', 'Chemical Engineering', 'LSAT', 'ACT', 'Music', 'Earth Sciences', 'Religious Studies', 'Engineering', 'Astronomy', 'Biomedical Engineering'],
     ['Negotiations', 'Chemical Engineering', 'LSAT', 'ACT', 'Music', 'Earth Sciences', 'Religious Studies', 'Engineering', 'Astronomy', 'Biomedical Engineering']),
    (9, ['Psychology', 'Marketing', 'Systems Engineering', 'Criminal Justice', 'ACT', 'Physics', 'Art History', 'Negotiations', 'Social Work', 'Chemistry'],
     ['Psychology', 'Systems Engineering', 'Criminal Justice', 'ACT', 'Physics', 'Art History', 'Negotiations', 'Social Work']),
    (15, [],
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
