// JavaScript - Node v8.1.3

describe('test counter', function() {
    var counter = new Counter();

    it('initialize', function() {
        Test.assertEquals(counter.getValue(), 0, 'Initial counter value must be 0');
    });

    it('increase', function() {
        counter.increase();
        Test.assertEquals(counter.getValue(), 1, 'Counter value must be increased');
    });

    it('reset', function() {
        counter.reset();
        Test.assertEquals(counter.getValue(), 0, 'Counter value must be 0 after reset');
    });
});
