// JavaScript - Node v8.1.3

describe('Default test cases', function() {
    it('Should work for test cases', function() {
        var n = '00-00..00-00';
        var m = 3;
        var sol = '            00-00..00-00\n      0000--0000....0000--0000\n000000---000000......000000---000000';
        Test.assertEquals(buildPyramid(n, m), sol, 'Should look like this: ');
        print(n, m, sol);

        m = 7;
        sol = '                                    00-00..00-00\n                              0000--0000....0000--0000\n                        000000---000000......000000---000000\n                  00000000----00000000........00000000----00000000\n            0000000000-----0000000000..........0000000000-----0000000000\n      000000000000------000000000000............000000000000------000000000000\n00000000000000-------00000000000000..............00000000000000-------00000000000000';
        Test.assertEquals(buildPyramid(n, m), sol, 'Should look like this: ' );
        print(n, m, sol);
    })
});

function print(n, m, sol) {
    console.log('<p style="color: red;">For width: ' + n + ' and height: ' + m + '</p>');
    console.log('Your solution: ');
    console.log(buildPyramid(n, m));
    console.log('</br>');
    console.log('How it should look like: ');
    console.log(sol);
}
