// JavaScript - Node v8.1.3

var arr = ['a', 'b', 'c', 'd', 'e'];
Test.assertSimilar(first(arr), ['a']);
Test.assertSimilar(first(arr, 2), ['a', 'b']);
Test.assertSimilar(first(arr, 3), ['a', 'b', 'c']);
Test.assertSimilar(first(arr, 0), []);
