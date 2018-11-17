// JavaScript - Node v8.1.3

suits = 'cdhs';
numbers = 'A23456789TJQK';

function encode(input) {
    function isValid(symbol) {
        if (typeof(symbol) !== 'string') {
            return false;
        }
        if (symbol.length !== 2) {
            return false;
        }
        return (numbers.indexOf(symbol[0]) !== -1) && (suits.indexOf(symbol[1]) !== -1);
    }

    output = [];
    for (var i in input) {
        var symbol = input[i];
        if (!isValid(symbol)) {
            return null;
        }
        output.push(suits.indexOf(symbol[1]) * 13 + numbers.indexOf(symbol[0]));
    }
    output.sort((a, b) => a - b);
    return output;
}

function decode(input) {
    function isValid(code) {
        if (typeof(code) !== 'number') {
            return false;
        }
        return (0 <= code) && (code < 52);
    }

    for (var i in input) {
        if (!isValid(input[i])) {
            return null;
        }
    }
    input.sort((a, b) => a - b);

    output = [];
    for (var i in input) {
        var code = input[i];
        var suit = suits[Math.floor(code / 13)];
        var number = numbers[code % 13];
        output.push(number + suit);
    }
    return output;
}

function cardsConverter(input) {
    if (!Array.isArray(input)) {
        return null;
    }
    if (input.length == 0) {
        return [];
    }

    if (typeof(input[0]) === 'string') {
        return encode(input);
    }
    else if (typeof(input[0]) === 'number') {
        return decode(input);
    }
    return null;
}
