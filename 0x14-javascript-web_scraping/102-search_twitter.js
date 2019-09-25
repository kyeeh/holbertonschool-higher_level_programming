#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const url = process.argv[2];
const file = process.argv[3];
const req = require('request');
const fileStream = require('fs');

req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fileStream.writeFile(file, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
