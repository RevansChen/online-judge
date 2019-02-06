# Python - 3.6.0

test.assert_equals(is_opposite('ab', 'AB'), True)
test.assert_equals(is_opposite('aB', 'Ab'), True)
test.assert_equals(is_opposite('aBcd', 'AbCD'), True)
test.assert_equals(is_opposite('AB', 'Ab'), False)
test.assert_equals(is_opposite('', ''), False)
