# Python - 2.7.6

Test.describe('lowercase_count')

Test.it('works for some examples')
Test.assert_equals(lowercase_count('abc'), 3)
Test.assert_equals(lowercase_count('abcABC123'), 3)
Test.assert_equals(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 3)
Test.assert_equals(lowercase_count(''), 0)
Test.assert_equals(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
Test.assert_equals(lowercase_count('abcdefghijklmnopqrstuvwxyz'), 26)
