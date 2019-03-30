// TypeScript - 2.4/ES6

/// <reference path="/runner/typings/mocha/index.d.ts" />
/// <reference path="/runner/typings/chai/index.d.ts" />
import { expect } from "chai";
import {
    Color,
    var1Boolean,
    var2Decimal,
    var3Hex,
    var4Binary,
    var5Octal,
    var6String,
    var7Array,
    var8NumericArray,
    var9Tuple,
    var10Enum,
    var11ArrayOfAny,
    var12VoidFunction,
    var13Null,
    var14Undefined,
    var15NeverFunction
} from "./solution";

describe("Checking variables", () => {
    it("var1Boolean should be equal to true", () => {
        expect(var1Boolean).to.equal(true);
    });
    it("var2Decimal should be equal to 13", () => {
        expect(var2Decimal).to.equal(13);
    });
    it("var3Hex should be equal to 0xf00d", () => {
        expect(var3Hex).to.equal(0xf00d);
    });
    it("var4Binary should be equal to 0b111111", () => {
        expect(var4Binary).to.equal(0b111111);
    });
    it("var5Octal should be equal to 0o744", () => {
        expect(var5Octal).to.equal(0o744);
    });
    it("var6String should be equal to 'Hello, world!'", () => {
        expect(var6String).to.equal('Hello, world!');
    });
    it("var7Array should be equal to [1, 'test', {a: 3}, 4, 5]", () => {
        expect(var7Array).to.deep.equal([1, 'test', { a: 3 }, 4, 5]);
    });
    it("var8NumericArray should be equal to [1, 2, 3, 4, 5]", () => {
        expect(var8NumericArray).to.deep.equal([1, 2, 3, 4, 5]);
    });
    it("var9Tuple should be equal to ['key', 12345]", () => {
        expect(var9Tuple).to.deep.equal(['key', 12345]);
    });
    it("var10Enum should be equal to Color.Blue", () => {
        expect(var10Enum).to.equal(Color.Blue);
    });
    it("var11ArrayOfAny should be equal to [1, 'test', {a: 3}, 4, 5]", () => {
        expect(var11ArrayOfAny).to.deep.equal([1, 'test', { a: 3 }, 4, 5]);
    });
    it("var12VoidFunction should be void function", () => {
        expect(typeof (var12VoidFunction)).to.equal('function');
        expect(var12VoidFunction()).to.equal(undefined);
    });
    it("var13Null should be equal to null", () => {
        expect(var13Null).to.equal(null);
    });
    it("var14Undefined should be equal to undefined", () => {
        expect(var14Undefined).to.equal(undefined);
    });
    it("var15NeverFunction should be never function", () => {
        expect(typeof (var15NeverFunction)).to.equal('function');
        try {
            expect(var15NeverFunction()).to.equal(undefined);
        }
        catch (e) {
        }
    });
});
