// JavaScript - Node v8.1.3

describe('Basic Tests', _ => {
    it('It should works for basic tests.', _ => {
        Test.assertEquals(cutCube(27, 27), true);
        Test.assertEquals(cutCube(512, 8), true);
        Test.assertEquals(cutCube(512, 64), true);
        Test.assertEquals(cutCube(50000, 50) , false);
        Test.assertEquals(cutCube(432, 16), false);
        Test.assertEquals(cutCube(256, 8), false);
        Test.assertEquals(cutCube(27, 3), false);
        Test.assertEquals(cutCube(123, 456), false);
        Test.assertEquals(cutCube(27, 8), false);
    });
});
