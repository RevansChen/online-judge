# Python - 3.6.0

Test.describe('Basic tests')
Test.it('None or Empty')
Test.assert_equals(sum_array(None), 0)
Test.assert_equals(sum_array([]), 0)

Test.it('Only one Element')
Test.assert_equals(sum_array([3]), 0)
Test.assert_equals(sum_array([-3]), 0)

Test.it('Only two Element')
Test.assert_equals(sum_array([3, 5]), 0)
Test.assert_equals(sum_array([-3, -5]), 0)

Test.it('Real Tests')
Test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
Test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
Test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
Test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)
