# Python - 3.6.0

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('partlist')
Test.it('Basic tests')
testing(partlist(['I', 'wish', 'I', 'hadn\'t', 'come']),
    [('I', 'wish I hadn\'t come'), ('I wish', 'I hadn\'t come'), ('I wish I', 'hadn\'t come'), ('I wish I hadn\'t', 'come')]
)
testing(partlist(['cdIw', 'tzIy', 'xDu', 'rThG']),
    [('cdIw', 'tzIy xDu rThG'), ('cdIw tzIy', 'xDu rThG'), ('cdIw tzIy xDu', 'rThG')]
)
testing(partlist(['vJQ', 'anj', 'mQDq', 'sOZ']),
    [('vJQ', 'anj mQDq sOZ'), ('vJQ anj', 'mQDq sOZ'), ('vJQ anj mQDq', 'sOZ')]
)
