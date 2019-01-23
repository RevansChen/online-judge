# Python - 2.7.6

Test.describe('Basic Tests')
data = [2]
Test.assert_equals(print_array(data), '2')

data = [2, 4, 5, 2]
Test.assert_equals(print_array(data), '2,4,5,2')

data = [2, 4, 5, 2]
Test.assert_equals(print_array(data), '2,4,5,2')

data = [2.0, 4.2, 5.1, 2.2]
Test.assert_equals(print_array(data), '2.0,4.2,5.1,2.2')

data = ['2', '4', '5', '2']
Test.assert_equals(print_array(data), '2,4,5,2')

data = [True, False, False]
Test.assert_equals(print_array(data), 'True,False,False')

array1 = ['hello', 'this', 'is', 'an', 'array!']
array2 = ['a', 'b', 'c', 'd', 'e!']
data = array1 + array2
Test.assert_equals(print_array(data), 'hello,this,is,an,array!,a,b,c,d,e!')

array1 = ['hello', 'this', 'is', 'an', 'array!']
array2 = [1, 2, 3, 4, 5]
data = [array1, array2]
Test.assert_equals(print_array(data), "['hello', 'this', 'is', 'an', 'array!'],[1, 2, 3, 4, 5]")
