from PIL import Image, ImageDraw, ImageFont

dado1 = "DISPÕE SOBRE A TRANSPARÊNCIA NO PROCESSO DE VACINAÇÃO CONTRA COVID - 19 EM TERESINA - PI POR MEIO DA OBRIGATORIEDADE DA PUBLICAÇÃO DIÁRIA DE LISTA DE TODOS OS VACINADOS."

dado2 = "Autor(es) da Proposição: Enzo Samuel"
dado3 = "Protocolo: Nº 356"
dado4 = "Data: 26/02/2021 13:08:15"
dado5 = "Projeto de Lei Ordinária N° 42 /2021"
dado6 = "Processo N°: 354 /2021"
dado7 = "Situação: Tramitando"
 
n = 40
dados_aux = []
dados_aux.append(dado1[:n])
dado1 = dado1[n:]
while len(dado1[n:]) > n:
    dados_aux.append(dado1[:n])
    dado1 = dado1[n:]
dados_aux.append(dado1)

img = Image.open('background.jpg')

 
fnt1 = ImageFont.truetype("C:\Windows\Fonts\Candara.ttf", 25)
fnt2 = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 25)

d = ImageDraw.Draw(img)

color = 'rgb(0, 0, 0)'

#linha1
d.text((20,20), dado2 ,  font=fnt1, fill=color)
d.text((500,20), dado3 , font=fnt1, fill=color)

#linha2
d.text((20,60), dado4 , font=fnt1, fill=color)
d.text((500,60), dado6 , font=fnt1, fill=color)

#linha3
d.text((20,100), dado5 , font=fnt1, fill=color)
d.text((500,100), dado7 , font=fnt1, fill=color)


k = 300

for dado in dados_aux:
    d.text((40,k), dado, align="left", font=fnt2, fill=color)
    k += 25
 
img.save('images/teste_projeto_de_lei.jpeg')