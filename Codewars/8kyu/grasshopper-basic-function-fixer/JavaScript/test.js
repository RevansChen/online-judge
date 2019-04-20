// JavaScript - Node v8.1.3

describe('fix add five', _ => {
    it('fixed tests', _ => {
        Test.assertEquals(addFive(5), 10);
        Test.assertEquals(addFive(0), 5);
        Test.assertEquals(addFive(-5), 0);
    });
});
