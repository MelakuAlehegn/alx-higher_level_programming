#!/usr/bin/node
const x = process.argv[2];
if (x) {
  for (let index = 0; index < x; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
