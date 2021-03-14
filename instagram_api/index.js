const Instagram = require('instagram-web-api')
require("dotenv").config({path: __dirname+'/.env'});
const path = require("path")
const fs = require('fs');

const { USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM } = process.env; 

const client = new Instagram({ username:USERNAME_INSTAGRAM, password:PASSWORD_INSTAGRAM })

function wait(ms){
  var start = new Date().getTime(); //verificar se é milisegundos
  var end = start;
  while(end < start + ms) {
    end = new Date().getTime();
 }
}

(async () => {
  await client.login()
  const {paths} = require("./paths.json")

  paths.forEach(async (p) => {
      await client.uploadPhoto({photo: p, caption: "#custopiaui  #leisteresina", post: 'feed' }).catch(error => { console.log("Deu Erro",error)})
      wait(10000)   
  });

 
})()