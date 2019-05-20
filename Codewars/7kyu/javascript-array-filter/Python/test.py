# Python - 3.6.0

@test.describe('Sample Tests')
def sample_tests():
    test_data = [
        ([2, 4, 5, 6], [2, 4, 6]),
        ([], []),
        ([1], []),
        ([1, 2], [2]),
        ([1, 2, 3, 4, 5], [2, 4]),
        ([2, 4, 6, 8], [2, 4, 6, 8])
    ]
    for data, exp in test_data:
        actual = get_even_numbers(data)
        test.assert_equals(type(actual), type([]), 'Did not return a list')
        test.assert_equals(len(actual) if type(actual) == type([]) else None, len(exp), 'Returned list has an incorrect length')
        test.assert_equals(actual, exp, 'Returned list has incorrect values')
