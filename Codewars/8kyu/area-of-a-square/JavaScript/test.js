// JavaScript - Node v8.1.3

Test.describe("squareArea(2)", function() {
    Test.assertEquals(squareArea(2), 1.62);
});

Test.describe("squareArea(0)", function() {
    Test.assertEquals(squareArea(0), 0);
});

Test.describe("squareArea(14.05)", function() {
    Test.assertEquals(squareArea(14.05), 80);
});
