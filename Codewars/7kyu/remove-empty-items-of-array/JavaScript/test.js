// JavaScript - Node v10.x

describe('Basic Tests', () => {
    it('Good stuff', () => {
        Test.assertDeepEquals(clean([]), [], 'Empty Array');
        Test.assertDeepEquals(clean(Array(500000)), [], '5000000 empty items');
        Test.assertDeepEquals(clean([1, 2]), [1, 2], 'No empty items here');
        Test.assertDeepEquals(clean([1, 2, , , 3, 4,]), [1, 2, 3, 4], 'Two Empty Items');
        Test.assertDeepEquals(clean([1, 2, [], , 3]), [1, 2, [], 3], 'Sub-Arrays');
    });
    
    it('Works Against Falsey Values', () => {
        Test.assertDeepEquals(clean([undefined, null, NaN, false, '', 0]), [undefined, null, NaN, false, '', 0], 'Falsey Values');
        Test.assertDeepEquals(clean([undefined, , , , null, , NaN, , false, '', 4, 3, 2, 1, 0]), [undefined, null, NaN, false, '', 4, 3, 2, 1, 0], 'Falsey, Empty, Truthy');
    });
});
