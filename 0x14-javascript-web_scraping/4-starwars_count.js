#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const url = process.argv[2];
const req = require('request');

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes('18')) counter++;
      }
    }
    console.log(counter);
  }
});
