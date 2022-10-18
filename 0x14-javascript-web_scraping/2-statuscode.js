#!/usr/bin/node
// a script that display the status code of a GET request
const request = require('request');
const URL = process.argv[2];
request(URL, function (response) {
  console.log('code:', response && response.statusCode);
});
