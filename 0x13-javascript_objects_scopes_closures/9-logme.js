#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  console.log(item, count);
  count++;
};
