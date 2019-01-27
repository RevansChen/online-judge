# Python - 2.7.6

Test.describe('Basic tests')
Test.assert_equals(shorten_to_date('Monday February 2, 8pm'), 'Monday February 2')
Test.assert_equals(shorten_to_date('Tuesday May 29, 8pm'), 'Tuesday May 29')
Test.assert_equals(shorten_to_date('Wed September 1, 3am'), 'Wed September 1')
Test.assert_equals(shorten_to_date('Friday May 2, 9am'), 'Friday May 2')
Test.assert_equals(shorten_to_date('Tuesday January 29, 10pm'), 'Tuesday January 29')
