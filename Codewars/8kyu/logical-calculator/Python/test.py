# Python - 2.7.6

Test.describe('Basic tests')
Test.assert_equals(logical_calc([True, False], 'AND'), False)
Test.assert_equals(logical_calc([True, False], 'OR'), True)
Test.assert_equals(logical_calc([True, False], 'XOR'), True)

Test.assert_equals(logical_calc([True, True, False], 'AND'), False)
Test.assert_equals(logical_calc([True, True, False], 'OR'), True)
Test.assert_equals(logical_calc([True, True, False], 'XOR'), False)
