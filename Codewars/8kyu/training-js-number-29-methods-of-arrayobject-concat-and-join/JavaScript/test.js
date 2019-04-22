// JavaScript - Node v8.1.3

Test.assertSimilar(bigToSmall([[1, 2], [3, 4], [5, 6]]), '6>5>4>3>2>1');
Test.assertSimilar(bigToSmall([[1, 3, 5], [2, 4, 6]]), '6>5>4>3>2>1');
Test.assertSimilar(bigToSmall([[1, 1], [1], [1, 1]]), '1>1>1>1>1');
