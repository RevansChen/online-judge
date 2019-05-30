# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(replicate(3, 5), [5, 5, 5])
Test.assert_equals(replicate(5, 1), [1, 1, 1, 1, 1])
Test.assert_equals(replicate(0, 12), [])
Test.assert_equals(replicate(-1, 12), [])
Test.assert_equals(replicate(8, 0), [0, 0, 0, 0, 0, 0, 0, 0])
