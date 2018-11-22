# Python - 3.6.0

def run_test(arr, n, s=''): test.assert_equals(find_needle(arr), 'found the needle at position %d' % n, s)

run_test(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False], 3)
run_test(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago'], 5)
run_test([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54], 30)
