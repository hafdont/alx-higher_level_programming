#!/usr/bin/node
const x = parseInt(process.argv[2]);

if (!Number.isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C if sun');
  }
} else {
  console.log('Missing number of occurrences');
}
