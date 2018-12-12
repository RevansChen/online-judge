// JavaScript - Node v8.1.3

describe('vowel', () => {
    it('Basic tests', () => {
        Test.assertEquals(''.vowel(), false);
        Test.assertEquals('a'.vowel(), true);
        Test.assertEquals('E'.vowel(), true);
        Test.assertEquals('ou'.vowel(), false);
        Test.assertEquals('z'.vowel(), false);
        Test.assertEquals('lol'.vowel(), false);
    });
});
