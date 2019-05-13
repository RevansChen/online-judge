# Python - 3.6.0

Test.it('Sample tests')

tablet = [
    ['S', 'T', 'A', 'B'],
    ['T', 'U', 'B', 'A'],
    ['A', 'B', 'U', 'T'],
    ['B', 'A', 'T', 'S']
]
Test.assert_equals(is_sator_square(tablet), True)

tablet = [
    ['K', 'N', 'I', 'T'],
    ['N', 'O', 'R', 'I'],
    ['I', 'R', '0', 'N'],
    ['T', 'I', 'N', 'K']
]
Test.assert_equals(is_sator_square(tablet), False)
