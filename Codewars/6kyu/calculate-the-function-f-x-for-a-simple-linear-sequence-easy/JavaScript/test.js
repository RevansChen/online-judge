// JavaScript - Node v8.1.3

Test.assertEquals(getFunction([0, 1, 2, 3, 4]), 'f(x) = x', 'Nope! Try again.');
Test.assertEquals(getFunction([0, 3, 6, 9, 12]), 'f(x) = 3x', 'Nope! Try again.');
Test.assertEquals(getFunction([1, 4, 7, 10, 13]), 'f(x) = 3x + 1', 'Nope! Try again.');
