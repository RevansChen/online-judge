# Python - 3.6.0

def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe('wallpaper')
Test.it('Basic tests')
testing(wallpaper(6.3, 4.5, 3.29), 'sixteen')
testing(wallpaper(7.8, 2.9, 3.29), 'sixteen')
testing(wallpaper(6.3, 5.8, 3.13), 'seventeen')
testing(wallpaper(6.1, 6.7, 2.81), 'sixteen')
