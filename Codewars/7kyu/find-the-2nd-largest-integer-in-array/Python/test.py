# Python - 3.6.0

test.describe('Example Tests')
test.assert_equals(find_2nd_largest([1, 2, 3]), 2, 'Expected 2')
test.assert_equals(find_2nd_largest([1, 1, 1, 1, 1, 1, 1]), None, 'expected None')
test.assert_equals(find_2nd_largest([1, 'a', '2', 3, 3, 4, 5, 'b']), 4, 'expected 4')
test.assert_equals(find_2nd_largest([1, 'a', '2', 3, 3, 3333333333333333333334, 544444444444444444444444444444, 'b']), 3333333333333333333334, 'expected 3333333333333333333334')
