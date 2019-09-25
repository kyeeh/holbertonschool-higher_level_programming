#!/usr/bin/node
// script that writes a string to a file

const str = process.argv[3];
const filepath = process.argv[2];
const fileStream = require('fs');
fileStream.writeFile(filepath, str, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
