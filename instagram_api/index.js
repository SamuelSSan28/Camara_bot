const Instagram = require('instagram-web-api')
require("dotenv").config({path: __dirname+'/.env'});
const path = require("path")
const fs = require('fs');

const { USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM } = process.env; 

const client = new Instagram({ username:USERNAME_INSTAGRAM, password:PASSWORD_INSTAGRAM })

function wait(ms){
  return new Promise(resolve => setTimeout(resolve, ms));
}

const write_log = (error_message) =>{
  var data = new Date();
  fs.appendFile("logs.txt",error_message+" -- "+data+"\n", function (err) {
    if (err) return console.log("ERROROROROOROR");
  });
}


(async() => {
  const {paths} = require("./paths.json")
  await client.login()

  for (const path of paths) {
    try {
      var data = new Date();
      var time_string = data.getHours() + ":" +data.getMinutes() + ":" + data.getSeconds();

      await client.uploadPhoto({photo: path, caption: "#custopiaui  #leisteresina "+time_string, post: 'feed' })

      await wait(120*1000)   

      fs.unlink(path, (err) => {
          if (err) {
            write_log("Erro ao deletar a imagem"+err)
          }
      });

    } catch (err) {
      write_log("Erro na requisiçaõ"+err)
    }
  
  }
 
})()