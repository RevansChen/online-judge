# Python - 3.6.0

gets = lambda i: 's' if i != 1 else ''
HQ9 = {
    'H': 'Hello World!',
    'Q': 'Q',
    '9': '\n'.join(
        f'{i} bottle{gets(i)} of beer on the wall, {i} bottle{gets(i)} of beer.\nTake one down and pass it around, {i - 1 if i > 1 else "no more"} bottle{gets(i - 1)} of beer on the wall.' for i in range(99, 0, -1)
    ) + '\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
}.get
