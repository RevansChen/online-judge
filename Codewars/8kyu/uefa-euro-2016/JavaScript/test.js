// JavaScript - Node v8.1.3

Test.assertEquals(uefaEuro2016(['Germany', 'Ukraine'], [2, 0]), 'At match Germany - Ukraine, Germany won!');
Test.assertEquals(uefaEuro2016(['Belgium', 'Italy'], [0, 2]), 'At match Belgium - Italy, Italy won!');
Test.assertEquals(uefaEuro2016(['Portugal', 'Iceland'], [1, 1]), 'At match Portugal - Iceland, teams played draw.');
