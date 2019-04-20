// JavaScript - Node v8.1.3

Test.describe('generateRange(2, 10, 2)', _ => {
    Test.assertSimilar(generateRange(2, 10, 2), [2, 4, 6, 8, 10]);
});
