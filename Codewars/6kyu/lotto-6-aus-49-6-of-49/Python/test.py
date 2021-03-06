# Python - 3.6.0

Test.describe('Basic tests')
winning_numbers = number_generator()
Test.assert_equals(len(winning_numbers), 7, 'The method must return an array of 7 numbers.')
Test.assert_equals(winning_numbers[6] >= 0 and winning_numbers[6] <= 9, True, 'The Superzahl must be between 0 and 9.')
Test.assert_not_equals(number_generator(), winning_numbers, 'The numbers have to be random!')
Test.assert_equals(len(set(winning_numbers[:6])), 6, 'No doublettes allowed in the first 6 numbers.')
Test.assert_equals(winning_numbers[:6], sorted(winning_numbers[:6]), 'The first 6 numbers have to be in ascending order.')
Test.assert_equals(all(a >= 1 and a <= 49 for a in winning_numbers[:6]), True, 'The base numbers must be between 1 and 49.')
Test.assert_equals(winning_numbers[6] >= 0 and winning_numbers[6] <= 9, True, 'The superzahl must be between 0 and 9')
Test.assert_equals(check_for_winning_category([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]), 1)
Test.assert_equals(check_for_winning_category([1, 2, 3, 4, 5, 6, 0], [1, 2, 3, 4, 5, 6, 7]), 2)
Test.assert_equals(check_for_winning_category([1, 2, 3, 34, 35, 39, 1], [1, 2, 3, 4, 5, 6, 7]), 8)
Test.assert_equals(check_for_winning_category([11, 12, 13, 34, 35, 39, 1], [1, 2, 3, 4, 5, 6, 7]), -1)
Test.assert_equals(check_for_winning_category([1, 12, 13, 34, 35, 39, 1], [1, 2, 3, 4, 5, 6, 1]), -1)
