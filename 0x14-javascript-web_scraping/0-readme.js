#!/usr/bin/node
// reads and prints the content of a file.

const file = process.argv[2];
const fileStream = require('fs');
fileStream.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
