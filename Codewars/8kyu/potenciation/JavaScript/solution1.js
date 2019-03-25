// JavaScript - Node v8.1.3

const power = (x, y) => ((y < 0) ? -(y & 1) : 1) * Array(Math.abs(y)).fill(x).reduce((a, b) => a * b, 1);
