// JavaScript (ES6)

function buildPalindrome(st) {
    function isPalindrome(s) {
        for (var i = 0; i < Math.ceil(s.length / 2); ++i) {
            if (s[i] != s[s.length - i - 1]) {
                return false;
            }
        }
        return true;
    }

    var adding = '';
    for (var i in st) {
        if (isPalindrome(st + adding)) {
            break;
        }
        adding = st[i] + adding;
    }
    return st + adding;
}
