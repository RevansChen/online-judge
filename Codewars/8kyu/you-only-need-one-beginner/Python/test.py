# Python - 3.4.3

test.describe('Example Tests')
tests = [
    (True, ((66, 101), 66)),
    (False, ((78, 117, 110, 99, 104, 117, 107, 115), 8)),
    (True, ((101, 45, 75, 105, 99, 107), 107)),
    (True, ((80, 117, 115, 104, 45, 85, 112, 115), 45)),
    (True, (('t', 'e', 's', 't'), 'e')),
    (False, (('what', 'a', 'great', 'kata'), 'kat')),
    (True, ((66, 'codewars', 11, 'alex loves pushups'), 'alex loves pushups')),
    (False, (('come', 'on', 110, '2500', 10, '!', 7, 15), 'Come')),
    (True, (("when's", 'the', 'next', 'Katathon?', 9, 7), 'Katathon?')),
    (False, ((8, 7, 5, 'bored', 'of', 'writing', 'tests', 115), 45)),
    (True, (('anyone', 'want', 'to', 'hire', 'me?'), 'me?'))
]

for exp, inp in tests:
    test.assert_equals(check(*inp), exp)
