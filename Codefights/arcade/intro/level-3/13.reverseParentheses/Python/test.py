# Python3

from solution1 import reverseParentheses as f

qa = [
    ('a(bc)de', 'acbde'),
    ('a(bcdefghijkl(mno)p)q', 'apmnolkjihgfedcbq'),
    ('co(de(fight)s)', 'cosfighted'),
    ('Code(Cha(lle)nge)', 'CodeegnlleahC'),
    ('Where are the parentheses?', 'Where are the parentheses?'),
    ('abc(cba)ab(bac)c', 'abcabcabcabc'),
    ('The ((quick (brown) (fox) jumps over the lazy) dog)', 'The god quick nworb xof jumps over the lazy')
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
