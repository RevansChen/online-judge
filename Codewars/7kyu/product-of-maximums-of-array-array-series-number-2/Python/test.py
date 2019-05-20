# Python - 3.6.0

Test.it('Basic Tests')
test.assert_equals(max_product([0] * 10, 5), 0)
test.assert_equals(max_product([4, 3, 5], 2), 20)
test.assert_equals(max_product([10, 8, 7, 9], 3), 720)
test.assert_equals(max_product([8, 6, 4, 6], 3), 288)

Test.it('Larger arrays')
test.assert_equals(max_product([*range(10, -1, -1)], 5), 10 * 9 * 8 * 7 * 6)
test.assert_equals(max_product([10, 2, 3, 8, 1, 10, 4], 5), 9600)
test.assert_equals(max_product([13, 12, -27, -302, 25, 37, 133, 155, -1], 5), 247895375)

Test.it('Arrays with negative values')
test.assert_equals(max_product([-4, -27, -15, -6, -1], 2), 4)
test.assert_equals(max_product([-17, -8, -102, -309], 2), 136)

Test.it('Arrays with positive and negative values')
test.assert_equals(max_product([10, 3, -27, -1], 3), -30)
test.assert_equals(max_product([14, 29, -28, 39, -16, -48], 4), -253344)
