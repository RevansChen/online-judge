// JavaScript - Node v8.1.3

Test.describe('decompose', function() {
    Test.it('works for some examples', function() {
        Test.assertSimilar(decompose(0), [[], 0]);
        Test.assertSimilar(decompose(4), [[2], 0]);
        Test.assertSimilar(decompose(9), [[3], 1]);
        Test.assertSimilar(decompose(25), [[4, 2], 0]);
        Test.assertSimilar(decompose(8330475), [[22, 13, 10, 8, 7, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2], 0]);
        Test.assertSimilar(decompose(9819938), [[23, 12, 9, 8, 6, 6, 5, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 0]);
        Test.assertSimilar(decompose(8331299), [[22, 13, 10, 8, 7, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2], 199]);
        Test.assertSimilar(decompose(8328441), [[22, 13, 10, 8, 7, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 50]);
    });
});
