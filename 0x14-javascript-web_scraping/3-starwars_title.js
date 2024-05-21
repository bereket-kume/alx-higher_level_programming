#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
    return;
  }
  data = JSON.parse(data);
  console.log(data.title);
});
