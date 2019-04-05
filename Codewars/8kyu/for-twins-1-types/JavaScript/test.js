// JavaScript - Node v8.1.3

Test.describe('Basic Tests', _ => {
    Test.assertEquals(typeValidation(42, 'number'), true);
    Test.assertEquals(typeValidation('42', 'number'), false);
});
