#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (error, _, body) => {
    if (error) {
      console.log(error);
    }
    const charsURL = JSON.parse(body).characters;
    const charsName = charsURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (ErrorProm, __, charactersReqBody) => {
          if (ErrorProm) {
            reject(ErrorProm);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charsName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
