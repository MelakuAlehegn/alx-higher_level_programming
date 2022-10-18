#!/usr/bin/node
const request = require('request');
const movie = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movie}`;
request(url, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (err, res, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
