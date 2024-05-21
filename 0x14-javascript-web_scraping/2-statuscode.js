#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res) => {
  if (err) {
    console.log(err);
    return;
  }
  if (res) {
    console.log('code:', res.statusCode);
  }
});
