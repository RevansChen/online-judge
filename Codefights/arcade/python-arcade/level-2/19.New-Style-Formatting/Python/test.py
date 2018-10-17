# Python3

from solution1 import newStyleFormatting as f

qa = [
    ('We expect the %f%% growth this week',
     'We expect the {}% growth this week'),
    ('%d%d%%-growth in products is expected quite soon',
     '{}{}%-growth in products is expected quite soon'),
    ('Much %%s we have here!',
     'Much %s we have here!'),
    ('Nothing to insert.',
     'Nothing to insert.'),
    ('New style formatting (like %s) is waay cooler than old-style (i.e. %s)',
     'New style formatting (like {}) is waay cooler than old-style (i.e. {})'),
    ('%%%%x',
     '%%x'),
    ('%%%%%d',
     '%%{}')
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
