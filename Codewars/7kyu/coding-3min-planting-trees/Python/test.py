# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(sc(3, 3, 1), 4)
Test.assert_equals(sc(3, 3, 3), 2)
Test.assert_equals(sc(3, 3, 2), 0)
Test.assert_equals(sc(7, 7, 3), 6)
Test.assert_equals(sc(3, 3, 0), 8)
Test.assert_equals(sc(3, 3, 10), 0)
Test.assert_equals(sc(2, 2, 1), 2)
Test.assert_equals(sc(2, 2, 0), 4)
Test.assert_equals(sc(200, 2, 1), 200)
Test.assert_equals(sc(2, 200, 1), 200)
