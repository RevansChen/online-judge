# Python - 3.6.0

Test.describe('Basic tests')
Test.assert_equals(goose_filter(['Mallard', 'Hook Bill', 'African', 'Crested', 'Pilgrim', 'Toulouse', 'Blue Swedish']), ['Mallard', 'Hook Bill', 'Crested', 'Blue Swedish'])
Test.assert_equals(goose_filter(['Mallard', 'Barbary', 'Hook Bill', 'Blue Swedish', 'Crested']), ['Mallard', 'Barbary', 'Hook Bill', 'Blue Swedish', 'Crested'])
Test.assert_equals(goose_filter(['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']), [])
