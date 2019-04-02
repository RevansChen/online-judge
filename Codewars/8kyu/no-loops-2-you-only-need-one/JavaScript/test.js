// JavaScript - Node v8.1.3

Test.describe('Basic tests', _ => {
    Test.assertEquals(check([66, 101], 66), true);
    Test.assertEquals(check([80, 117, 115, 104, 45, 85, 112, 115], 45), true);
    Test.assertEquals(check(['t', 'e', 's', 't'], 'e'), true);
    Test.assertEquals(check(['what', 'a', 'great', 'kata'], 'kat'), false);
})
