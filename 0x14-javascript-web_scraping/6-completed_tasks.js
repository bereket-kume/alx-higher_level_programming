#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  body = JSON.parse(body);
  const userDict = {};
  for (let i = 0; i < body.length; i++) {
    if (body[i].completed) {
      if (!(body[i].userId in userDict)) {
        userDict[body[i].userId] = 1;
      } else {
        userDict[body[i].userId] += 1;
      }
    }
  }
  console.log(userDict);
});
