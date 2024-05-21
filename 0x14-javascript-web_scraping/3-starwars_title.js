#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(url, (_err, _res, data) => {
  data = JSON.parse(data);
  console.log(data.title);
});
