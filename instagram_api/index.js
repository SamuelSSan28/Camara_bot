const Instagram = require('instagram-web-api')
require("dotenv").config({path: __dirname+'/.env'});
const path = require("path")
const fs = require('fs');

const { USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM } = process.env; 

const client = new Instagram({ username:USERNAME_INSTAGRAM, password:PASSWORD_INSTAGRAM })

function wait(ms){
  var start = new Date().getTime();
  var end = start;
  while(end < start + ms) {
    end = new Date().getTime();
 }
}

;(async () => {
  await client.login()

  const file_path = path.join(__dirname,"..",'gerar_imagens','paths.txt')

  fs.readFile(file_path, 'utf8', async (err,data)=> {
    if (err) {
      return console.log("Deu erro");
    }

    const lines = data.split(/\r?\n/);
    
    // print all lines
    lines.forEach(async (line) => {
        const [image,vereador] = line.split(",") //nao deu certo
        
        const image_path  = path.join(__dirname,"..",'gerar_imagens',image)

        // Upload Photo to feed or story, just configure 'post' to 'feed' or 'story'
        await client.uploadPhoto({ photo: image_path, caption: vereador, post: 'feed' }).catch(error => { console.log("Deu Erro")})

        wait(3000)
        console.log("Atual: ",image_path);       
       
    });
    
  });

 
})()