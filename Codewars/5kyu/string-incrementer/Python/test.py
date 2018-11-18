# Python - 3.6.0

Test.assert_equals(increment_string('foo'), 'foo1')
Test.assert_equals(increment_string('foobar001'), 'foobar002')
Test.assert_equals(increment_string('foobar1'), 'foobar2')
Test.assert_equals(increment_string('foobar00'), 'foobar01')
Test.assert_equals(increment_string('foobar99'), 'foobar100')
Test.assert_equals(increment_string('foobar099'), 'foobar100')
Test.assert_equals(increment_string(''), '1')
