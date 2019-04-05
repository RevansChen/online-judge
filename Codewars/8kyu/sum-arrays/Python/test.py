# Python - 3.6.0

test.describe('Testing sum_array')

test.assert_equals(sum_array([]), 0)
test.assert_equals(sum_array([1, 2, 3]), 6)
test.assert_equals(sum_array([1.1, 2.2, 3.3]), 6.6)
test.assert_equals(sum_array([4, 5, 6]), 15)
test.assert_equals(sum_array(range(101)), 5050)
