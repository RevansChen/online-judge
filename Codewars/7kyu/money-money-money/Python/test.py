# Python - 2.7.6

Test.describe('calculate_years')

Test.it('works for some examples')
Test.assert_equals(calculate_years(1000, 0.05, 0.18, 1100), 3)
Test.assert_equals(calculate_years(1000, 0.01625, 0.18, 1200), 14)
Test.assert_equals(calculate_years(1000, 0.05, 0.18, 1000), 0)
