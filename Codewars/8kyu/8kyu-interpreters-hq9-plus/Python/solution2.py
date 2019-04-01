# Python - 3.6.0

gets = lambda i: 's' if i != 1 else ''
getn = lambda i: f'{i if i > 0 else "no more" if i == 0 else 99} bottle{gets(i)}'
getm = lambda i: 'Go to the store and buy some more' if i <= 0 else 'Take one down and pass it around'
getl1 = lambda i: f'{getn(i)} of beer on the wall, {getn(i)} of beer.'.capitalize()
getl2 = lambda i: f'{getm(i)}, {getn(i - 1)} of beer on the wall.'.capitalize()
HQ9 = {
    'H': 'Hello World!',
    'Q': 'Q',
    '9': '\n'.join(
        '\n'.join([getl1(i), getl2(i)]) for i in range(99, -1, -1)
    )
}.get
