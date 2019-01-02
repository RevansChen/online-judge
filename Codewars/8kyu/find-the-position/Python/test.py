# Python - 3.6.0

test.describe('Example Tests')

tests = [
    # [input, expected]
    ['a', 'Position of alphabet: 1'],
    ['z', 'Position of alphabet: 26'],
    ['e', 'Position of alphabet: 5']
]

for inp, exp in tests:
    test.assert_equals(position(inp), exp)
