// JavaScript - Node v8.1.3

const arr2bin = (arr) => arr.reduce((a, b) => a + ((typeof(b) === 'number') ? b : 0), 0).toString(2);
