const nodeHtmlToImage = require('node-html-to-image');
const path = require("path")
const fs = require('fs');

const create_images = async(dados) => {
  var paths = [];

  for (var key in dados) {
    if (dados.hasOwnProperty(key)) {
        var autores_li = "";

        const path = `./instagram_api/image/image_${dados[key].protocolo}.jpeg`

        paths.push(path);

        for (const element of dados[key].autores){
            autores_li += `<li class="item">${element}</li>`
        }
        
        await nodeHtmlToImage({
          output: path,
          html: `
          <html>
          <meta charset="utf-8"/>
          <link rel="preconnect" href="https://fonts.gstatic.com">
          <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">

          <head>
            <style type = "text/css">
                p { font-family: 'Roboto', sans-serif; color: #FFF; font-size: 35px; text-align: justify; }
                li { font-family: 'Roboto', sans-serif; color: #FFF; font-size: 35px; }
                body{
                    background-image: url("https://i.imgur.com/3iS3ZrO.jpg");
                    -webkit-flex: 1; flex: 1;
                    height: 1080px;
                    width: 1080px;
                    padding: 20px;
                    background-size: cover;
                }

                #top{
                  margin-top: 20px;
                  padding: 50px;
                  height: 20%;
                  -webkit-flex: 1; flex: 1;
                    width: 100%;
                }
                
                #mid{
                  font-weight:bold;
                  background: rgba(0, 0, 0, 0.75);
                  display: -webkit-flex; 
                  flex-direction: row-center;
                  align-items: center;
                  justify-content: center;
                  padding: 50px;
                  height: 50%;
                  -webkit-flex: 1; flex: 1;
                    width: 100%;
                }
                #bot{
                  padding: 50px;
                  height: 30%;
                  -webkit-flex: 1; flex: 1;
                    width: 100%;
                }
                * {
                    -webkit-box-sizing: border-box;
                  }
                  .flexrow {
                    display: -webkit-flex;
                    display: flex;
                    flex-direction: column;
                    flex-wrap: wrap;
                    justify-content: space-between;
                  }
                  .flexrow2 {
                    
                    display: flex;

                    flex-wrap: wrap;
                    justify-content: space-between;
                  }
                  .item {
                    margin: 5px;
                    text-align: center;
                    font-size: 1.8em;
                    }
          

              </style>
          </head>
          <body class="flexrow">
          
          <div id="top">
            <p>Data: ${dados[key].data}</p>
                
            <p>${dados[key].tipo}</p>

            <p>Situação: ${dados[key].situacao}</p>
          </div>

          <div id="mid">
            <div id="texto">
              <p>${dados[key].resumo}</p>
            </div>
          </div>

          <div id="bot">
              <p>Autor(es) da Proposição: </p>

            <ul class="flexrow2">
              ${autores_li}
            </ul>
          </div>

          </body>
          </html>
          `
        }).then(() => {
          
        })
    }
  }

  dictstring= JSON.stringify({"paths":paths})
  fs.writeFile("./instagram_api/paths.json", dictstring, function (err) {
    if (err) return console.log("\n***\n")
  });
}

const write_log = (error_message) =>{
  fs.appendFile("logs.txt",error_message+" -- "+data+"\n", function (err) {
    if (err) return console.log("ERROROROROOROR");
  });
}

try {
  const dados = require('../dados.json'); 
  console.log("---Gerando as imagens---\n")
  create_images(dados);
} catch (err) {
  write_log("Erro ao criar as imagens"+err)
}