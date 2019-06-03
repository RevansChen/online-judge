# Python - 3.6.0

test.describe('Example Tests')

test.assert_equals(scramble('abcd', [0, 3, 1, 2]), 'acdb', 'Should return acdb')
test.assert_equals(scramble('sc301s', [4, 0, 3, 1, 5, 2]), 'c0s3s1', 'Should return c0s3s1')
test.assert_equals(scramble('bskl5', [2, 1, 4, 3, 0]), '5sblk', 'Should return 5sblk')
