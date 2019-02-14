# Python - 3.6.0

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('arrange')
Test.it('Basic tests')
testing(arrange('who hit retaining The That a we taken'), 'who RETAINING hit THAT a THE we TAKEN')
testing(arrange('on I came up were so grandmothers'), 'i CAME on WERE up GRANDMOTHERS so')
testing(arrange('way the my wall them him'), 'way THE my WALL him THEM')
testing(arrange('turn know great-aunts aunt look A to back'), 'turn GREAT-AUNTS know AUNT a LOOK to BACK')
