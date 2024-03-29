#!/usr/bin/node
// a script that computes the number of tasks completed by user id

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const myDict = JSON.parse(body).reduce((acc, elem) => {
    if (!acc[elem.userId]) {
      if (elem.completed) {
        acc[elem.userId] = 1;
      }
    } else {
      if (elem.completed) {
        acc[elem.userId] += 1;
      }
    }
    return acc;
  }, {});
  console.log(myDict);
});
