# Python - 2.7.6

Test.describe('Basic tests')
Test.assert_equals(to_freud('test'), 'sex')
Test.assert_equals(to_freud('sexy sex'), 'sex sex')
Test.assert_equals(to_freud('This is a test'), 'sex sex sex sex')
Test.assert_equals(to_freud('This is a longer test'), 'sex sex sex sex sex')
Test.assert_equals(to_freud("You're becoming a true freudian expert"), 'sex sex sex sex sex sex')
