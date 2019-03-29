// JavaScript - Node v8.1.3

describe('Basic Tests', function() {
    it('It should works for basic tests.', function() {
        Test.assertEquals(isValid([1, 3, 7]), true);
        Test.assertEquals(isValid([7, 1, 2, 3]), false);
        Test.assertEquals(isValid([1, 3, 5, 7]), false);
        Test.assertEquals(isValid([1, 5, 6, 7, 3]), true);
        Test.assertEquals(isValid([5, 6, 7]), true);
        Test.assertEquals(isValid([5, 6, 7, 8]), true);
        Test.assertEquals(isValid([6, 7, 8]), false);
        Test.assertEquals(isValid([7, 8]), true);
    })
})
