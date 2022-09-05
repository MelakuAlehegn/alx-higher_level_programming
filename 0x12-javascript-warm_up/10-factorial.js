#!/usr/bin/node
const c1 = process.argv[2];
function factorial (c1) {
  if (isNaN(c1) || c1 === 1) {
    return (1);
  } else {
    return (c1 * factorial(c1 - 1));
  }
}
console.log(factorial(parseInt(c1)));
