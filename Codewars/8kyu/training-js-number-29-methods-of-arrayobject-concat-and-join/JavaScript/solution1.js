// JavaScript - Node v8.1.3

const bigToSmall = arr => [].concat(...arr).sort((a, b) => b - a).join('>');
