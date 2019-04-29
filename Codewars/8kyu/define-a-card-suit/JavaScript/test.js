// JavaScript - Node v8.1.3

Test.describe('Basic tests', () => {
    Test.assertEquals(defineSuit('3♣'), 'clubs');
    Test.assertEquals(defineSuit('Q♠'), 'spades');
    Test.assertEquals(defineSuit('9♦'), 'diamonds');
    Test.assertEquals(defineSuit('J♥'), 'hearts');
});
