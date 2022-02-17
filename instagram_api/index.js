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

(async() => {
  const {paths} = require("./paths.json")

  try {
    await client.login()
  } catch(err) {
    if (err.error && err.error.message === 'checkpoint_required') {
      const challengeUrl = err.error.checkpoint_url
      await client.updateChallenge({ challengeUrl, choice: 1  })
    }
  }

  console.log("...")
  for (const path of paths) {
    try {    
      await client.uploadPhoto({photo: path, caption: "#custopiaui  #leisteresina ", post: 'feed' })
      
      await wait(300)   

      await fs.unlink(path, (err) => {
          if (err) {
            write_log("Erro ao deletar a imagem"+err)
          }
      });


    } catch (err) {
      var data = new Date();
      var error_message = "Erro na api do instagram: "+err
      fs.appendFile("logs.txt",error_message+" -- "+data+"\n", function (err) {
        if (err) return console.log("Erro ao apagar o arquivo");
      });
    }
  }

  const dictstring = JSON.stringify({"paths":[]});
  await fs.writeFile("./instagram_api/paths.json", dictstring, function (err) {
    if (err) return console.log("\n***\n",err)
  });
  console.log("Postado no Instagram")

 
})()