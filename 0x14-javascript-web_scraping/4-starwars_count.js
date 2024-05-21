#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wid = '18';
function strarwarsCount (url, id) {
  request(url, (err, _res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)) {
        count++;
      }
    });
    console.log(count);
  });
}
strarwarsCount(url, wid);
