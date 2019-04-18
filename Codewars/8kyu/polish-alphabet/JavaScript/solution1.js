// JavaScript - Node v8.1.3

const correctPolishLetters = string => {
    let from = 'ąćęłńóśźż';
    let to   = 'acelnoszz';
    return Array.from(string).map(c => (from.indexOf(c) !== -1) ? to[from.indexOf(c)] : c).join('');
}
