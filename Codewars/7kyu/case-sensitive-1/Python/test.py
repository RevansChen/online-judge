# Python - 3.6.0

test.describe('Basic Tests')
test.it('Sample Tests')
test.assert_equals(case_sensitive('asd'), [True, []])
test.assert_equals(case_sensitive('cellS'), [False, ['S']])
test.assert_equals(case_sensitive('z'), [True, []])
test.assert_equals(case_sensitive(''), [True, []])

