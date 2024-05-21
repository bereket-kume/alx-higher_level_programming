#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

function fetchCharacters (characters, index = 0) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], (err, _res, body) => {
    if (err) {
      console.error(err);
      return;
    }
    const characterName = JSON.parse(body).name;
    console.log(characterName);
    fetchCharacters(characters, index + 1);
  });
}

request(url, (err, _res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  fetchCharacters(characters);
});
