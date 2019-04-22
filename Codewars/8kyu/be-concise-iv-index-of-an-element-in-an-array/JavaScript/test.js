// JavaScript - Node v8.1.3

describe('Your refactored find() function', _ => {
    it('should behave as expected', _ => {
        var array = [2, 3, 5, 7, 11];
        Test.assertEquals(find(array, 5), 2);
        Test.assertEquals(find(array, 11), 4);
        Test.assertEquals(find(array, 3), 1);
        Test.assertEquals(find(array, 2), 0);
        Test.assertEquals(find(array, 7), 3);
        Test.assertEquals(find(array, 1), 'Not found');
        Test.assertEquals(find(array, 8), 'Not found');
        array = [true, 'Hello World', false, 'Lorem Ipsum', 6, Math.PI];
        Test.assertEquals(find(array, 'Hello World'), 1);
        Test.assertEquals(find(array, 'lorem ipsum'), 'Not found');
        Test.assertEquals(find(array, 'Lorem Ipsum'), 3);
        Test.assertEquals(find(array, false), 2);
        Test.assertEquals(find(array, true), 0);
        Test.assertEquals(find(array, Math.PI), 5);
        Test.assertEquals(find(array, 3.14), 'Not found');
        Test.assertEquals(find(array, 6), 4);
    });
});
