# Python - 3.6.0

test.describe('Test of greek_comparator')
test.expect(greek_comparator('alpha', 'beta') < 0, 'result should be negative')
test.assert_equals(greek_comparator('chi', 'chi'), 0)
test.expect(greek_comparator('upsilon', 'rho'), 'result should be positive')
