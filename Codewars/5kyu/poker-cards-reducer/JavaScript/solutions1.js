// JavaScript - Node v8.1.3

suits = 'cdhs';
numbers = 'A23456789TJQK';

function getSortSymbols(input) {
    function isValid(symbol) {
        if (typeof(symbol) !== 'string') {
            return false;
        }
        if (symbol.length !== 2) {
            return false;
        }
        return (numbers.indexOf(symbol[0]) !== -1) && (suits.indexOf(symbol[1]) !== -1);
    }
    
    output = []
    for (var i in input) {
        symbol = input[i];
        if (!isValid(symbol)) {
            return null;
        }
        output.push(numbers.indexOf(symbol[0]));
    }
    output.sort((a, b) => a - b);
    for (var i in output) {
        output[i] = numbers[output[i]];
    }
    return output;
}

function getSortCodes(input) {
    function isValid(code) {
        if (typeof(code) !== 'number') {
            return false;
        }
        return (0 <= code) && (code < 52);
    }

    output = []
    for (var i in input) {
        code = input[i];
        if (!isValid(code)) {
            return null;
        }
        output.push(code % 13);
    }
    output.sort((a, b) => a - b);
    return output;
}

function reduceCards(input) {
    if (!Array.isArray(input)) {
        return null;
    }
    if (input.length === 0) {
        return [];
    }
    
    if (typeof(input[0]) === 'string') {
        return getSortSymbols(input);
    }
    else if (typeof(input[0]) === 'number') {
        return getSortCodes(input);
    }
    return null;
}
