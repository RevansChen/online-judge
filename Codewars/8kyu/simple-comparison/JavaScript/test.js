// JavaScript - Node v8.1.3

Test.assertEquals(add('1', 1), true);
Test.assertEquals(add(1, '1'), true);
Test.assertEquals(add(1, '0'), false);
Test.assertEquals(add('11', 11), true);
Test.assertEquals(add(12, 12), true);
Test.assertEquals(add(120, '021'), false);
