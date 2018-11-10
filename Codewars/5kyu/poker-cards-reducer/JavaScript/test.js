// JavaScript - Node v8.1.3

Test.assertSimilar(reduceCards('asdf'), null, 'should return null');
Test.assertSimilar(reduceCards([]), [], 'should return []');
Test.assertSimilar(reduceCards(['Td', 'Qd', '8c', 'Ac', 'Ks', 'Qs']), ['A', '8', 'T', 'Q', 'Q', 'K'], 'should return ["A", "8", "T", "Q", "Q", "K"]');
Test.assertSimilar(reduceCards([51, 7, 24, 22, 50, 0]), [0, 7, 9, 11, 11, 12], 'should return [0, 7, 9, 11, 11, 12]');
