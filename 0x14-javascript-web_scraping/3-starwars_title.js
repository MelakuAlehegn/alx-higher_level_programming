#!/usr/bin/node
// a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
const request = require('request');
const id = process.argv[2];
request(`https://swapi-api.hbtn.io/api/films/${id}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('body:', JSON.parse(body).title);
});
