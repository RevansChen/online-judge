# Python - 3.6.0

Test.it('Basic tests')
Test.assert_equals(check_exam(['a', 'a', 'b', 'b'], ['a', 'c', 'b', 'd']), 6)
Test.assert_equals(check_exam(['a', 'a', 'c', 'b'], ['a', 'a', 'b', '' ]), 7)
Test.assert_equals(check_exam(['a', 'a', 'b', 'c'], ['a', 'a', 'b', 'c']), 16)
Test.assert_equals(check_exam(['b', 'c', 'b', 'a'], ['' , 'a', 'a', 'c']), 0)
