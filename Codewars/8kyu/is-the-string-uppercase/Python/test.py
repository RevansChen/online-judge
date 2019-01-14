# Python - 3.6.0

def gen_test_case(inp, res):
    test.assert_equals(is_uppercase(inp), res, inp)

test.describe('Basic Tests')

gen_test_case('c', False)
gen_test_case('C', True)
gen_test_case('hello I AM DONALD', False)
gen_test_case('HELLO I AM DONALD', True)
