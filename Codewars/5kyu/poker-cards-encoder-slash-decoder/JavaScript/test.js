// JavaScript - Node v8.1.3

Test.assertSimilar(cardsConverter([50, 6, 13, 30, 37]), ["7c", "Ad", "5h", "Qh", "Qs"], 'should return ["7c", "Ad", "5h", "Qh", "Qs"]');
Test.assertSimilar(cardsConverter(["5h", "7c", "Qh", "Qs", "Ad"]), [6, 13, 30, 37, 50], 'should return [6, 13, 30, 37, 50]');
