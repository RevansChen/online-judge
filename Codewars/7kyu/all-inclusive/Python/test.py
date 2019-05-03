# Python - 3.6.0

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('contain_all_rots')
Test.it('Basic tests')
testing(contain_all_rots('', []), True)
testing(contain_all_rots('', ['bsjq', 'qbsj']), True)
testing(contain_all_rots('bsjq', ['bsjq', 'qbsj', 'sjqb', 'twZNsslC', 'jqbs']), True)
testing(contain_all_rots('XjYABhR', ['TzYxlgfnhf', 'yqVAuoLjMLy', 'BhRXjYA', 'YABhRXj', 'hRXjYAB', 'jYABhRX', 'XjYABhR', 'ABhRXjY']), False)
