// JavaScript - Node v8.1.3

Test.assertEquals(any([1, 2, 3, 4], function(v, i) { return v > 3; }), true);
Test.assertEquals(any([1, 2, 3, 4], function(v, i) { return v > 4; }), false);
