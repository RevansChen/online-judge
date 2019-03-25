// JavaScript - Node v8.1.3

Test.describe('Basic tests', () => {
    Test.assertEquals(typeOfSum(12, 1), 'number');
    Test.assertEquals(typeOfSum('d', 1), 'string');
    Test.assertEquals(typeOfSum(1, 'a'), 'string');
    Test.assertEquals(typeOfSum('dd', ''), 'string');
    Test.assertEquals(typeOfSum(true, 1), 'number');
    Test.assertEquals(typeOfSum('s', false), 'string');
    Test.assertEquals(typeOfSum(null, 1), 'number');
    Test.assertEquals(typeOfSum('s', null), 'string');
    Test.assertEquals(typeOfSum(null, undefined), 'number');
    Test.assertEquals(typeOfSum(undefined, 're'), 'string');
    Test.assertEquals(typeOfSum(undefined, true), 'number');
    Test.assertEquals(typeOfSum(null, false), 'number');
});

