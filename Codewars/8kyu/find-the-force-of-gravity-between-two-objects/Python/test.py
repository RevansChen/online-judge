# Python - 3.6.0

Test.describe('Tests')
test.it('Sample tests')
test.assert_approx_equals(solution([1000, 1000, 100], ['g', 'kg', 'm']), 6.67e-12)
test.assert_approx_equals(solution([1000, 1000, 100], ['kg', 'kg', 'm']), 6.667e-9)
test.assert_approx_equals(solution([1000, 1000, 100], ['kg', 'kg', 'cm']), 0.0000667)
