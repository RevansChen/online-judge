// JavaScript - Node v8.1.3

Test.assertEquals(greaterThanLessThan(Number(null), 0, 1), true);
Test.assertEquals(greaterThanLessThan(700000000001, 700000000002, -1), false);
Test.assertEquals(greaterThanLessThan(-9, -8, 7), true);
Test.assertEquals(greaterThanLessThan(-9, -8, -7), false);
