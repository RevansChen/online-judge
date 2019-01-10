# Python - 3.6.0

Test.describe('Valid number of animals')
Test.assert_equals(animals(72, 200), (44, 28))
Test.assert_equals(animals(116, 282), (91, 25))
Test.assert_equals(animals(12, 24), (12, 0))
Test.assert_equals(animals(6, 24), (0, 6))
Test.assert_equals(animals(344, 872), (252, 92))
Test.assert_equals(animals(158, 616), (8, 150))


Test.describe('Invalid number of animals')
Test.assert_equals(animals(25, 555), 'No solutions')
Test.assert_equals(animals(12, 25), 'No solutions')
Test.assert_equals(animals(54, 956), 'No solutions')
Test.assert_equals(animals(5455, 54956), 'No solutions')


Test.describe('Edge cases')
Test.assert_equals(animals(0, 0), (0, 0))
Test.assert_equals(animals(-1, -1), 'No solutions')
Test.assert_equals(animals(500, 0), 'No solutions')
Test.assert_equals(animals(0, 500), 'No solutions')
Test.assert_equals(animals(-45, 5), 'No solutions')
Test.assert_equals(animals(5, -55), 'No solutions')
