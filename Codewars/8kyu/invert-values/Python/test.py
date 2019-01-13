# Python - 3.4.3

Test.it('Basic Tests')
Test.assert_equals(invert([1, 2, 3, 4, 5]), [-1, -2, -3, -4, -5])
Test.assert_equals(invert([1, -2, 3, -4, 5]), [-1, 2, -3, 4, -5])
Test.assert_equals(invert([]), [])
