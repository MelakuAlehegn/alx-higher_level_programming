#!/usr/bin/node
// a script that read and print the conteint of a file
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', function (err, inputD) {
  if (err) throw err;
  console.log(inputD);
});
