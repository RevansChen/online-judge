# Python - 3.6.0

test.describe('Static Cases')
test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')
