// TypeScript - 2.4/ES3

/// <reference path="/runner/typings/main/ambient/mocha/index.d.ts" />
/// <reference path="/runner/typings/main/ambient/chai/index.d.ts" />
import solution = require('./solution');

// import the type of assertion library you wish to use (Chai recommended)
import {assert} from "chai";

describe("Testing multiply", function() {
    it("Should return a result", function() {
        assert.equal(solution.multiply(0, 1), 0);
        assert.equal(solution.multiply(1, 1), 1);
        assert.equal(solution.multiply(2, 2), 4);
        assert.equal(solution.multiply(3, 3), 9);
        assert.equal(solution.multiply(4, 3), 12);
        assert.equal(solution.multiply(5, 3), 15);
        assert.equal(solution.multiply(10, 8), 80);
        assert.equal(solution.multiply(10, 10), 100);
        assert.equal(solution.multiply(10, -10), -100);
        assert.equal(solution.multiply(-10, 10), -100);
        assert.equal(solution.multiply(-10, -10), 100);
        assert.equal(solution.multiply(20, 10), 200);
    });
});