#!/usr/bin/node
const axios = require('axios');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

axios.get(apiUrl + movieId)
  .then((response) => {
    const characters = response.data.characters;
    console.log(characters);
  })
  .catch((error) => {
    console.error('Error:', error.message);
  });
