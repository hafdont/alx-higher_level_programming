#!/usr/bin/node
function findSecondMax (args) {
  if (args.length <= 1) {
    return 0;
  }
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
  }
  return secondMax;
}

const args = process.argv.slice(2);
console.log(findSecondMax(args));
