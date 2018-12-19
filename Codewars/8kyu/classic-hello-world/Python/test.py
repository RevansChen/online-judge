# Python - 2.7.6

Test.describe('Basic tests')
#the preloaded testing functions calls the function and compares what
#it prints with the result parameter
Test.it('Testing with no extra parameter')
test_solution_main(Solution.main, result = 'Hello World!')
Test.it("Testing with 'Hola mundo!' as extra parameter")
test_solution_main(Solution.main, ['Hola mundo!'], result = 'Hello World!')
