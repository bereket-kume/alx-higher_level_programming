#!/usr/bin/node

const args = process.argv.slice(2).map(Number);


if (args.length < 2) {
  console.log(0);
} else {
  let biggest = args[0];
  let secondBiggest = args[1];

  for (let i = 2; i < args.length; i++) {
    if (args[i] > biggest) {
      secondBiggest = biggest;
      biggest = args[i];
    } else if (args[i] > secondBiggest && args[i] < biggest) {
      secondBiggest = args[i];
    }
  }

  console.log(secondBiggest);
}
