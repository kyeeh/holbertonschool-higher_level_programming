#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  list = process.argv.sort()
  console.log(list[list.length - 2]);
}
