// JavaScript - Node v8.1.3

Test.describe("Simple input", function() {
    var input = [1, 2, 3, 4, 5];

    Test.it("Should only mirror numbers greater than four", function() {
        var mappers = [
            [ function (i) { return i > 4; },
              function (i) { return i; } ],
            [ function (i) { return i; },
              function (i) { return "x"; } ]
        ];

        Test.assertSimilar(mapEmUp(input, mappers), ["x", "x", "x", "x", 5], "Maps number correctly");
    });
});
