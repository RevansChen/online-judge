# Python - 2.7.6

# Grab the print output from the program as a list of lines.
# result2 is the array of lines from Python 2.7 print
# result3 is the array of lines from x_print
print_output_2, print_output_3 = printOuts.get_output()

test.describe('Python 2 Tests')
test.assert_equals(print_output_2[0], 'Hello World!', "Print 'Hello World!' correctly")
test.assert_equals(print_output_2[1], 'Welcome to CIS 122: Intro to Software Design', 'Print course welcome correctly')
test.assert_equals(print_output_2[2], 'The sum of 1.1 and 3 is 4.1', 'Print sum of a + b correctly')

test.describe('Python 3 Tests')
test.assert_equals(print_output_3[0], 'Hello World!', "Print 'Hello World!' correctly")
test.assert_equals(print_output_3[1], 'Learning Python is Fun', 'Print observation correctly')
test.assert_equals(print_output_3[2], 'There are 80 slices in 10 pizzas.', 'Print slice count correctly')
test.assert_equals(print_output_3[3], '80: It must be dinner time!', 'Print dinner message correctly')

test.describe('Variables Correctly Named and Used')
test.assert_equals(name, 'Intro to Software Design', "Correctly used 'name' variable.")
test.assert_equals(a, 1.1, "Correctly used 'a' variable.")
test.assert_equals(b, 3, "Correctly used 'b' variable.")
test.assert_equals(c, 4.1, "Correctly used 'c' variable.")
test.assert_equals(language, 'Python', "Correctly used 'language' variable.")
test.assert_equals(adjective, 'Fun', "Correctly used 'adjective' variable.")
test.assert_equals(pizzas, 10, "Correctly used 'pizzas' variable.")
test.assert_equals(slices_per_pizza, 8, "Correctly used 'slices_per_pizza' variable.")
test.assert_equals(total_slices, 80, "Correctly used 'total_slices' variable.")
