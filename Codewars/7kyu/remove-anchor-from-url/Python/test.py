# Python - 3.6.0

@test.describe('Sample tests')
def fixed_tests():
    Test.assert_equals(remove_url_anchor('www.codewars.com#about'), 'www.codewars.com')
    Test.assert_equals(remove_url_anchor('www.codewars.com/katas/?page=1#about'), 'www.codewars.com/katas/?page=1')
    Test.assert_equals(remove_url_anchor('www.codewars.com/katas/'), 'www.codewars.com/katas/')
