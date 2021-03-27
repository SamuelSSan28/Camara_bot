const Instagram = require('instagram-web-api')
require("dotenv").config({path: __dirname+'/.env'});
const path = require("path")
const fs = require('fs');

const { USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM,USERNAME_INSTAGRAM_TESTE, PASSWORD_INSTAGRAM_TESTE , ENVIROMENT_APP} = process.env; 

const client = new Instagram( ENVIROMENT_APP == "PROD" ? 
  { username:USERNAME_INSTAGRAM, password:PASSWORD_INSTAGRAM }
  :
  { username:USERNAME_INSTAGRAM_TESTE, password:PASSWORD_INSTAGRAM_TESTE }
  )

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
  console.log("Postando no Instagram")
  for (const path of paths) {
    try {    
      await client.uploadPhoto({photo: path, caption: "#custopiaui  #leisteresina ", post: 'feed' })

      await wait(600*1000)   

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