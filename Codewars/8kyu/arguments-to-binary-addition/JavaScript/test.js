// JavaScript - Node v8.1.3

Test.assertEquals(arr2bin([1, 2]), '11');
Test.assertEquals(arr2bin([1, 2, 3, 4, 5]), '1111');
Test.assertEquals(arr2bin([1, 10, 100, 1000]), '10001010111');
Test.assertEquals(arr2bin([null]), '0');
Test.assertEquals(arr2bin([true, true, false, 15]), '1111');
