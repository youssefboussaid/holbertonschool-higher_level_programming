#!/usr/bin/node
const args = process.argv[2];
if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args; i++) {
    console.log('X'.repeat(args));
  }
}
