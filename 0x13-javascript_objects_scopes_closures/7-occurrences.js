#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const a in list) {
    if (list[a] === searchElement) {
      count++;
    }
  }
  return count;
};
