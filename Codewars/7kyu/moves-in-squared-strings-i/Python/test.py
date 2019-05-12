# Python - 3.6.0

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('opstrings')
Test.it('Basic tests vert_mirror')
testing(oper(vert_mirror, 'hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu'), 'QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw')
testing(oper(vert_mirror, 'IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx'), 'EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP')

Test.it('Basic tests hor_mirror')
testing(oper(hor_mirror, 'lVHt\nJVhv\nCSbg\nyeCt'), 'yeCt\nCSbg\nJVhv\nlVHt')
testing(oper(hor_mirror, 'njMK\ndbrZ\nLPKo\ncEYz'), 'cEYz\nLPKo\ndbrZ\nnjMK')
