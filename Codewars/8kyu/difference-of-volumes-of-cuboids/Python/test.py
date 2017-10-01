# Python - 3.4.3

Test.describe('Basic tests')

testcases = [
    ([3, 2, 5], [1, 4, 4], 14),
    ([9, 7, 2], [5, 2, 2], 106)
]
for a, b, ans in testcases:
    rt = find_difference(a, b)
    Test.expect(rt == ans, "%d should equal %d" % (rt, ans))