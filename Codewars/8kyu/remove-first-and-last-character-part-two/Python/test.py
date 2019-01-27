# Python - 2.7.6

Test.describe('Basic Tests')
Test.assert_equals(array(''), None)
Test.assert_equals(array('1'), None)
Test.assert_equals(array('1, 3'), None)
Test.assert_equals(array('1,2,3'), '2')
Test.assert_equals(array('1,2,3,4'), '2 3')
