# Python - 3.6.0

Test.describe('what_is')
Test.it('should work correctly')
tests = [
    (0, 'nothing'),
    (123, 'nothing'),
    (-1, 'nothing'),
    (42, 'everything'),
    (42 * 42, 'everything squared')
]

for x, answer in tests:
    Test.assert_equals(what_is(x), answer)
