// JavaScript - Node v8.1.3

var ft1 = createArgumentMap(function(){});
Test.expect(Object.keys(ft1).length == 0, 'Should return []');

var ft2 = createArgumentMap(function(a1){}, 'a1 argvalue');
Test.expect(Object.keys(ft2).length == 1, 'Should have 1 element');
Test.expect(ft2['a1'] === 'a1 argvalue', "Should return 'a1 argvalue'");
