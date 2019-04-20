// JavaScript - Node v8.1.3

const generateRange = (min, max, step) => Array.from({length: Math.floor((max - min) / step) + 1}, (v, i) => (min + i * step));
