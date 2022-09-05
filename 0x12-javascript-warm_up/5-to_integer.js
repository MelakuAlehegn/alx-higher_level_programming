#!/usr/bin/node
const c1 = process.argv[2];
if (isNaN(c1) || c1 === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(c1));
}
