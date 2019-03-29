# Python - 3.6.0

test.describe('Example Tests')

tests = (
    ('John', 'Hello, John!'),
    ('aLIce', 'Hello, Alice!'),
    ('', 'Hello, World!')
)

for inp, exp in tests:
    test.assert_equals(hello(inp), exp)

test.assert_equals(hello(), 'Hello, World!')
