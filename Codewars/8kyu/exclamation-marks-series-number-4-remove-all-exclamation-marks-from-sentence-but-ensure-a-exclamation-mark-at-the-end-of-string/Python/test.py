# Python - 3.6.0

test.describe('Basic Tests')

tests = [
    ['Hi!', 'Hi!'],
    ['Hi!!!','Hi!'],
    ['!Hi', 'Hi!'],
    ['!Hi!', 'Hi!'],
    ['Hi! Hi!', 'Hi Hi!'],
    ['Hi', 'Hi!']
]

for inp, exp in tests:
    test.assert_equals(remove(inp), exp)
