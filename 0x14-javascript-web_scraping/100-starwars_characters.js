#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (err, _res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (er, _re, inbody) => {
      if (er) {
        console.log(er);
        return;
      }
      const charname = JSON.parse(inbody).name;
      console.log(charname);
    });
  }
});
