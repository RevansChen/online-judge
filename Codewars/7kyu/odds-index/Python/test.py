# Python - 3.6.0

Test.it('Basic tests')
Test.assert_equals(odd_ball(['even', 4, 'even', 7, 'even', 55, 'even', 6, 'even', 10, 'odd', 3, 'even']), True)
Test.assert_equals(odd_ball(['even', 4, 'even', 7, 'even', 55, 'even', 6, 'even', 9, 'odd', 3, 'even']), False)
Test.assert_equals(odd_ball(['even', 10, 'odd', 2, 'even']), True)
