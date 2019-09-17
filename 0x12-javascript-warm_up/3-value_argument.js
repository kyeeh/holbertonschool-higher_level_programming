#!/usr/bin/node
// prints the first argument passed to it

if (process.argv.length === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
