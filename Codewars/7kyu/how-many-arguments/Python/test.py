# Python - 3.6.0

test.describe('Basic tests')
test.assert_equals(args_count(100), 1)
test.assert_equals(args_count(100, 2, 3), 3)
test.assert_equals(args_count(32, a1 = 12), 2)
test.assert_equals(args_count(), 0)
