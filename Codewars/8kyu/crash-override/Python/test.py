# Python - 3.6.0

basic_tests = (
    (('Mike', 'Millington'), 'Malware Mike'),
    (('Fahima', 'Tash'), 'Function T-Rex'),
    (('Daisy', 'Petrovic'), 'Data Payload'),
    (('Barny', 'White'), 'Beta Worm'),
    (('Hank', 'Kutz'), 'Half-life Killer'),
    (('123abc', 'Pinkman'), 'Your name must start with a letter from A - Z.'),
    (('walter', 'white'), 'WiFi Worm')
)

for names, result in basic_tests:
    Test.it('{} {}'.format(*names))
    Test.assert_equals(alias_gen(*names), result)
