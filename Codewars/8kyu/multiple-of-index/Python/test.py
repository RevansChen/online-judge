# Python - 3.6.0

Test.it('Basic tests')
Test.assert_equals(multiple_of_index([22, -6, 32, 82, 9, 25]), [-6, 32, 25])
Test.assert_equals(multiple_of_index([68, -1, 1, -7, 10, 10]), [-1, 10])
Test.assert_equals(multiple_of_index([11, -11]), [-11])
Test.assert_equals(multiple_of_index([-56, -85, 72, -26, -14, 76, -27, 72, 35, -21, -67, 87, 0, 21, 59, 27, -92, 68]), [-85, 72, 0, 68])
Test.assert_equals(multiple_of_index([28, 38, -44, -99, -13, -54, 77, -51]), [38, -44, -99])
Test.assert_equals(multiple_of_index([-1, -49, -1, 67, 8, -60, 39, 35]), [-49, 8, -60, 35])
