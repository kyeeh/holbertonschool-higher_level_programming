#!/usr/bin/node
// script that prints the title of a Star Wars movie where the e9pisode number matches a given integer.

const req = require('request');
const episode = process.argv[2];
const url = 'http://swapi.co/api/films/' + episode;

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
