#!/usr/bin/node

const request = require('request');

Url = 'https://swapi-api.hbtn.io/api';
request(Url + '/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
