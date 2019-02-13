# Python - 3.6.0

test.assert_equals(is_triangle_number(3), True, f'Expected True for input 3.  Got {is_triangle_number(3)}.')
test.assert_equals(is_triangle_number(5), False, f'Expected False for input 5.  Got {is_triangle_number(5)}.')
test.assert_equals(is_triangle_number('hello!'), False, f'Expected False for input "hello!".  Got {is_triangle_number("hello!")}.')
test.assert_equals(is_triangle_number(6.15), False, f'Expected False for input 6.15.  Got {is_triangle_number(6.15)}.')
