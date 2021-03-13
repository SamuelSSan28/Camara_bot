const nodeHtmlToImage = require('node-html-to-image');
const path = require("path")
const fs = require('fs');

var autores = "";
var titulo = "";
var data = "";
var situacao = "";
var tipo = "";

const file_path = path.join(__dirname,"..",'novos_projetos.txt');




nodeHtmlToImage({
  output: './image.png',
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
          background: rgba(0, 0, 0, 0.5);
          display: -webkit-flex; 
          flex-direction: row-center;
          align-items: center;
          justify-content: center;
          padding: 50px;
          height: 60%;
          -webkit-flex: 1; flex: 1;
            width: 100%;
        }
        #bot{
          padding: 50px;
          height: 20%;
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
            display: -webkit-flex;
            display: flex;

            flex-wrap: wrap;
            justify-content: space-between;
          }

      </style>
  </head>
  <body class="flexrow">
  
  <div id="top">
     <p>Data: ${data}</p>
        
     <p>${tipo}</p>

     <p>Situação: ${situacao}</p>
  </div>

  <div id="mid">
    <div id="texto">
      <p>${titulo}</p>
    </div>
  </div>

  <div id="bot">
      <p>Autor(es) da Proposição: </p>

    <ul class="flexrow2">
      ${autores}
    </ul>
  </div>

  </body>
  </html>
  `
}).then(() => console.log('The image was created successfully!'))