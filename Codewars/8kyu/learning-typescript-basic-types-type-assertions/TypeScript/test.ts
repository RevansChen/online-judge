// TypeScript - 2.4/ES6

/// <reference path='/runner/typings/mocha/index.d.ts' />
/// <reference path='/runner/typings/chai/index.d.ts' />

import {expect} from 'chai';
import {
    getResult,
    ErrorServerResult,
    SuccessServerResult
} from './solution';

describe('getResult', () => {
    it('should return correct results for SuccessServerResult', () => {
        var message = {'message': 'Hello, world!'};
        var success = new SuccessServerResult(200, message);
        expect(getResult(success)).to.deep.equal(message);
    });
    it('should return correct results for ErrorServerResult', () => {
        var message = 'Not found';
        var error = new ErrorServerResult(404, message);
        expect(getResult(error as any)).to.equal(message);
    });
});
