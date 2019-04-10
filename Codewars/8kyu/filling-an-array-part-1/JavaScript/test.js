// JavaScript - Node v8.1.3

describe('#arr creates a new array with the numbers 0 to N-1', _ => {
    it('should return an array', _ => Test.expect(arr() instanceof Array));
    it('should return a blank array when called with no argument', _ => Test.assertSimilar(arr(), []));
    it('should return 0 to 3 when called with 4', _ => Test.assertSimilar(arr(4), [0, 1, 2, 3]));
});
