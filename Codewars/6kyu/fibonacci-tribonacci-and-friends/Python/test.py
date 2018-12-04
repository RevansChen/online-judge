# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(Xbonacci([0, 1], 10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
Test.assert_equals(Xbonacci([1, 1], 10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
Test.assert_equals(Xbonacci([0, 0, 0, 0, 1], 10), [0, 0, 0, 0, 1, 1, 2, 4, 8, 16])
Test.assert_equals(Xbonacci([1, 0, 0, 0, 0, 0, 1], 10), [1, 0, 0, 0, 0, 0, 1, 2, 3, 6])
Test.assert_equals(Xbonacci([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256])
