#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
if (!Number.isNaN(num1) && !Number.isNaN(num2)) {
  console.log(add(num1, num2));
} else {
  console.log('NaN');
}
