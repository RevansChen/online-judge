// JavaScript - Node v8.1.3

Test.assertEquals(contamination('abc', 'z'), 'zzz');
Test.assertEquals(contamination('', 'z'), '');
Test.assertEquals(contamination('abc', ''), '');
Test.assertEquals(contamination('_3ebzgh4', '&'), '&&&&&&&&');
Test.assertEquals(contamination('//case', ' '), '      ');
