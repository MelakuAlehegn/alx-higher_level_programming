#!/usr/bin/node
const size = process.argv[2];

if (size && !isNaN(parseInt(size))) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}