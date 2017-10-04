# Python - 3.4.3

test.describe("Example Tests")
test.assert_equals(symmetric_point([0,0], [1,1]), [2, 2])
test.assert_equals(symmetric_point([2, 6], [-2, -6]), [-6, -18])
test.assert_equals(symmetric_point([10, -10], [-10, 10]), [-30, 30])
test.assert_equals(symmetric_point([1, -35], [-12, 1]), [-25, 37])
test.assert_equals(symmetric_point([1000, 15], [-7, -214]), [-1014, -443])
test.assert_equals(symmetric_point([0, 0], [0, 0]), [0, 0])