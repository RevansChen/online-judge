# Python - 3.6.0

animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
Test.describe('partition')
Test.assert_equals(partition(animals, lambda x: len(x) == 3), (['cat', 'dog', 'cow'], ['duck', 'donkey']))
