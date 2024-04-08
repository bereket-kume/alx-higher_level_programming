#!/usr/bin/node
if (!isNaN(process.argv[2])){
	console.log(`My number: ${Math.floor(Number(process.argv[2]))}`);
} else{
	console.log('Not a number');
}
