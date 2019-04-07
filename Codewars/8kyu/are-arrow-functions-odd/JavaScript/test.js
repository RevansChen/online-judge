// JavaScript - Node v8.1.3

Test.assertSimilar(odds([]), [], 'Should handle empty array');
Test.assertSimilar(odds([2, 4, 6]), [], 'Should handle array with even numbers only');
Test.assertSimilar(odds([1, 3, 5]), [1, 3, 5], 'Should handle array with odd numbers only');
Test.assertSimilar(odds([1, 2, 3, 4, 5, 6]), [1, 3, 5], 'Should handle mixed array');
