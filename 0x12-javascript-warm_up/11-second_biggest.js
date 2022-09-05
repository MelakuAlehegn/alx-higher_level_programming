#!/usr/bin/node
if (process.argv.length > 3) {
    const c1 = process.argv.slice(2).map(Number);
  
    c1.splice(c1.indexOf(Math.max.apply(null, c1)), 1);
    console.log(Math.max.apply(null, c1));
  } else {
    console.log(0);
  }