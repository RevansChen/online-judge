// JavaScript - Node v8.1.3

String.prototype.vowel = function() {
    return (/^[aeiou]$/i).test(this);
};
