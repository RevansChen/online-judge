// JavaScript - Node v8.1.3

Test.assertSimilar(sc(2), 'Aa~ Pa! Aa!', 'good luck!');
Test.assertSimilar(sc(6), 'Aa~ Aa~ Aa~ Aa~ Aa~ Pa! Aa!', 'good luck!');
Test.assertSimilar(sc(7), 'Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!', 'good luck!');
Test.assertSimilar(sc(10), 'Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!', 'good luck!');
Test.assertSimilar(sc(1), '', 'good luck!');
Test.assertSimilar(sc(-1), '', 'good luck!');
